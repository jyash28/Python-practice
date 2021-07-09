# exception handling
# try except else finally
while True:

    try:
        age = int(input("enter your age:"))
    except ValueError:
        print("maybe you entered string instead of bnumber , try againcode")
    except:
        print("unexcepted error")

if age <18:
    print("you can't play this game")
else:
    print("you can olay this game")