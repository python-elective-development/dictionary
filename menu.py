import func
import menu_functions

#menu = {1:'Home', 2:'About', 'Q': 'Quit'}
menu = []
def usr_input(name):
    npt = input("Hi " + name +", What do you want to do? \n(" + str(menu) + ")") 
    return npt.lower()

# def home(name):
#     string = 'Hi ' + name + ' This is my HOME page'
#     return string

# def about(name):
#     string = 'Hi ' + name + ' This is my ABOUT page'
#     return string

# def quit(name):
#     return "Goodbye " + name + " Sorry to see you go "

dict_of_functions = {}
# dict_of_functions = {'1':home, '2':about, 'q': quit }

#count = 0
for key, value in menu_functions.__dict__.items():
    if callable(value):
        dict_of_functions[key] = value
        menu.append(key)  

print(dict_of_functions)

usr_name = input('Hi, Tell us your name! : ')

i = "1"
while i != "q":
    i = usr_input(usr_name)
    func.clear_screen()
    print("=====================")

    print(dict_of_functions[i](usr_name))

    print("=====================")
