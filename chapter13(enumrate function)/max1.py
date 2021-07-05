student2 = [
    {"name":"harshit","score" :90,"age":28},
    {"name":"rohit","score" :70,"age":24},
    {"name":"yash","score" :80,"age":21}
]
print(max(student2 ,key=lambda item: item.get("score")))