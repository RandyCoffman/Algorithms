def fact(x):
 if x == 1:
    return 1
 else:
    return x * fact(x-1)
# calls and returns a x * x-1 and so on, for example 5 would be 5 * 4 * 3 * 2 * 1
print(fact(5))