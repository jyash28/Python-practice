from csv import DictWriter
with open("final.csv","w",newline="") as f:
    csv_writer = DictWriter(f,fieldnames =["firstname","lastname","age"])
    csv_writer.writeheader()
    csv_writer.writerows([
        {"firstname":"harshit","lastname":"vashista","age":500},
        {"firstname":"harshit","lastname":"vashista","age":500},
        {"firstname":"harshit","lastname":"vashista","age":500}
    ])