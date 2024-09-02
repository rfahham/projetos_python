def my_decorator(func):
    def wrapper():
        print(f"Running {func.__name__}")
        func()
        print("Complete")
    return wrapper

@my_decorator
def do_this():
    print("Doing This")

@my_decorator
def do_that():
    print("Doing That")

do_this()
do_that()