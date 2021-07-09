while True:
    try:
        number = int(input("enter a number"))

    except ValueError:
        print("please type integer !! s")
    except:
        print("unexpected error !!!")
    else:
        print(f"user input = {number}")
        break
    finally:
        print("finally blocks.......")
        