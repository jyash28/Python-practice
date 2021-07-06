def outer_func():
    def inner_func():
        print("inside inner function")
    return inner_func
var = outer_func()
var()