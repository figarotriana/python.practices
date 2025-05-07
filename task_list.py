import json
#json.dump(diccionario, archivo)       Guardar un diccionario en un archivo JSON:
#datos = json.load(archivo)            Leer datos desde un archivo JSON:

#colors for appeal
c_reset = "\033[0m"
c_yellow = "\033[93m"
c_red = "\033[1m \033[91m"
c_title = "\033[103m\033[90m\033[1m"
c_danger = "\033[97m\033[101m\033[1m"
                                    # for copy and paste {c_reset} {c_red} {c_title} {c_yellow}

#structure
class tasklistuser:
    def __init__(self, user, password, tasklist):
        self.user = user
        self.password = password
        self.tasklist = tasklist
#information

"""tasks = {
    Figaro : {
        password : 1234
    }
}""" #pending

#Info = json.dump(tasks)  (pending)

#Start, log in engine
start = "0"
while start.upper() not in ["A", "B"]:
    start = input(f"""{c_title}Welcome! {c_reset}
            please type your prefferred option
            {c_red}A:{c_reset} Log in
            {c_red}B:{c_reset} Sign up
            """ )
    if start.upper() == "A":
        print("pending")
        break
    elif start.upper() == "B":
        new_username = input("Please enter username: ")
        new_password = input("Please enter your password: ")
        password_confirmation = input("Please confirm your password: ")
        while new_password != password_confirmation:
            password_confirmation = input("Password confirmation doesn't match with Password, please try again: ")
        new_username = tasklistuser(new_username, new_password, {})
        break
    else:
        print ("option invalid, please try again")