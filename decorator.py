from functools import wraps
def log(func):
    @wraps(func)
    def wrapper (*args,**kwargs):
        print("%s",func.__name__)
        return func(*args,**kwargs)
    return wrapper

@log
def TimePrint():
    print("20171025")

if __name__ == '__main__':
    TimePrint()