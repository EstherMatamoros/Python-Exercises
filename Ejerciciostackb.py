
user_1 = {"nombre" : "Sara", "edad" : 27}
user_2 = {"nombre" : "Kev", "edad" : 26}
user_3 = {"nombre" : "Carl", "edad" : 25}
users = [ user_1, user_2, user_3]

print(user_1["nombre"])


for user in users:
    if user["edad"] > 26:
        print(user)
    
new_list = [user for user in users if user["edad"] > 26]

print(new_list)