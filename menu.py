import func
import menu_functions

menu = []
dict_of_functions = {}

for key, value in menu_functions.__dict__.items():
    if callable(value):
        dict_of_functions[key] = value
        menu.append(key)  

def usr_input(name):
    npt = input("Hi " + name +", What do you want to do? \n(" + str(menu) + ")") 
    return npt.lower()

## Console code

usr_name = input('Hi, Tell us your name! : ')

i = "1"
while i != "q":
    i = usr_input(usr_name)
    func.clear_screen()
    print("=====================")

    print(dict_of_functions[i](usr_name))

    print("=====================")
