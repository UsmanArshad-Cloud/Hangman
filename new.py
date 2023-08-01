import functools
list_1 = [1, 2, 3]
def func(x):
    return x*2
a=list(map(func,list_1))
print(a)