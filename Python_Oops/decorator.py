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


@outer_fn(10)
def jod_fn(a,b):
    return a+b

# jod_fn = decorator_fn(jod_fn,5)

print(jod_fn(9,8))


# if __name__ == "__main__":
#     print(jod_fn(3,4))