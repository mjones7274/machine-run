from textwrap import indent
from tkinter import *
import json
from cryptography.fernet import Fernet


# UI config variables
bg_color_min = "CornSilk1"
main_screen_bg_color = "CornSilk2"
button_bg_color = "CornSilk3"
button_forecolor = "Gray9"
message_forecolor = "Gray9"
message_forecolor_flash = "Gray65"

def display_config():
    labelConfig.config(text=json.dumps(get_config(),indent=4))

def create_config():
    config_text = textConfig.get("1.0",'end-1c')
    encrypt_config(config_text)
    labelMessage.config(text='Config file (machine_config.val) encrypted successfully')

def get_config():
    global error_message, init_error
    # needs config.val in the same directory
    # config.val is the encrypted string for all the secret config data
    config = ''
    try:
        input_file = 'machine_config.val'

        with open(input_file, 'rb') as f:
            data = f.read()

        encPart = str(data, "utf-8").split("valhalla")
        idx = len(encPart[0]) - int(encPart[1])
        byteData = bytes(encPart[0], "utf-8")
        key = byteData[idx:]
        encData = byteData[:idx]

        fernet = Fernet(key)
        decrypted = fernet.decrypt(encData)
        config = json.loads(decrypted)
    except:
        config = { "error": "Invalid Configuration" }
        init_error = True
        return config
    return config

def encrypt_config(json_string):
    ## Encryption Function
    from cryptography.fernet import Fernet
    import base64

    key = Fernet.generate_key()
    postkey = "valhalla" + str(len(key))
    savekey = key + bytes(postkey, 'utf-8')

    output_file = 'machine_config.val'

    fernet = Fernet(key)
    encrypted = fernet.encrypt(bytes(json_string,'utf-8'))
    outString = encrypted + savekey

    with open(output_file, 'wb') as f:
        f.write(outString)

# Set up UI Screen
root = Tk() #Main graphic element
root.title("Machine Run")
root.geometry('800x600')
root.configure(bg=main_screen_bg_color)
canvas = Canvas(root,
                width=800,
                height=600,
                bd=0, highlightthickness=00,
                highlightcolor="red",
                highlightbackground="green"
                )

btnGetConfig = Button(root,
                text ="Show Config",
                width=15,
                height=2,
                font=("Arial",12),
                foreground=button_forecolor,
                bg=button_bg_color,
                command = display_config)
btnGetConfig.grid(column=0, row=0)

labelConfig = Label(root,
                     font=("Arial", 12),
                     width=55,
                     height=15,
                     anchor='w',
                     justify='left'
                     )
labelConfig.grid(column=1, row=0)

btnSetConfig = Button(root,
                text ="Create Config",
                width=15,
                height=2,
                font=("Arial",12),
                foreground=button_forecolor,
                bg=button_bg_color,
                command = create_config)
btnSetConfig.grid(column=0, row=1)

textConfig = Text(root,
                     font=("Arial", 12),
                     width=55,
                     height=15
                     )
textConfig.grid(column=1, row=1)

labelMessage = Label(root,
                     font=("Arial", 12),
                     anchor='w',
                     bg=main_screen_bg_color
                     )
labelMessage.grid(column=0, row=2, columnspan=2)


root.mainloop()