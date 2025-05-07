import json
#json.dump(diccionario, archivo)       Guardar un diccionario en un archivo JSON:
#datos = json.load(archivo)            Leer datos desde un archivo JSON:

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

#Program display
start = 0
while start.upper() not in ["A", "B"]:
    start = input("""Welcome! 
            please type your prefferred option
            A: Log in
            B: Sign up
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