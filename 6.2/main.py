import time

#personal filter function
#go through the iterable and keep the item if the function return true
def my_filter(func, iter):
    if func is None:
        func = lambda x: x is True
    iter = [item for item in iter if func(item)]
    return iter

#read from the user numbers with ',' between each one
#return a list of only positive numbers
#using a map to convert all numbers to int
#using filter to leave only the positive numbers
def get_positive_numbers():
    numbers = input()
    return list(filter(lambda x: x > 0, map(int,numbers.split(','))))

#get a function and arguments(dynamic)
#save the current time
#calculate the function with the args
#check and return the time elapsed
def timer(func, *args):
    start = time.time()
    func(args)
    end = time.time()
    return (end - start)
