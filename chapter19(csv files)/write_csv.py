# writer DictWriter
from csv import writer
with open("file1.csv","w",newline="") as f:
    csv_writer = writer(f)
    # methods writerow, writerows
    #csv_writer.writerow(["name","country"])
    #csv_writer.writerow(["mohit","usa"])
    #csv_writer.writerow(["yash","india"])

    csv_writer.writerows([["name","country"],["mohit","usa"],["yash","india"]])