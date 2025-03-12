import time

def timer(func):
    def rapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return rapper
@timer
def example_function(n):
    time.sleep(n)


example_function(2)    