def outer_fn(c):
    def decorator_fn(func):
        def wrapper(a,b):
            print("calling main func")
            res = func(a,b) 
            res = res + c
            print("Main function executed")
            return res
        return wrapper
    return decorator_fn

# applying decorator on main function
@outer_fn(10)
def jod_fn(a,b):
    return a+b

#calling main function
if __name__ == "__main__":
    print(jod_fn(3,4))