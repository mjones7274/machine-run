import json
from cryptography.fernet import Fernet

class Encryption:
    def __init__(self):
        self.config = ''

    def get_config(self):
    # needs machine_config.val in the same directory
    # machine_config.val is the encrypted string for all the secret config data
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
        return config

    def encrypt_config(self,json_string):
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