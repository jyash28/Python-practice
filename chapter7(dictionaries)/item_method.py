user_info= {
    "name":"harshit" ,
    "age":24 ,
    "favorite movie":["DDLJ","gijoe"]
}
user_items = user_info.items()
print(user_items)
print(type(user_items))
for key , value in user_info.items():
     print(f"key is{key} and value is {value}")