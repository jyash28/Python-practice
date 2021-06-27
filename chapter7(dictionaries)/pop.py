user_info= {
    "name":"harshit" ,
    "age":24 ,
    "favorite_movie":["DDLJ","gijoe"]
}
popped_item=user_info.pop("favorite_movie")
print(f"popped item is {popped_item}")
print(user_info)