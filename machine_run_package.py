from tkinter import *
from lib.encryption import Encryption
import json

# create new object using encryption module
encryption = Encryption()

# UI config variables
main_screen_bg_color = "CornSilk2"
button_bg_color = "CornSilk3"
button_forecolor = "Gray9"
message_forecolor = "Gray9"
message_forecolor_flash = "Gray65"

def display_config():
    labelConfig.config(text=json.dumps(encryption.get_config(),indent=4))

def create_config():
    config_text = textConfig.get("1.0",'end-1c')
    encryption.encrypt_config(config_text)
    labelMessage.config(text='Config file (machine_config.val) encrypted successfully')

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