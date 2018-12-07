dic = {1: 'Claus', 2: 'Julie', 3: 'Hannah', 4 : 'Esther' }
# print(dic)
# dic[0] = 'Tove'
# print(dic)

def my_func(name):
    return "Hello " + name

# dic[0] = my_func("Claus")
# dic[1] = my_func("Anna")
# dic[2] = my_func("Loise")
# dic[3] = my_func("Julie")
# dic[4] = my_func("Pia")
dic[5] = my_func("Tove")
dic[6] = my_func("Tanny")
dic[7] = my_func("Tom")
dic[8] = my_func
dic[9] = my_func
dic[10] = my_func

print(dic[10]("HENNING"))

for x, y in dic.items():
    print(x, end=" ")
    print(y, end=", ")        
    print("", end="\n\n")

# i = 0
# while i <= len(dic):
#     print(dic[i]())





