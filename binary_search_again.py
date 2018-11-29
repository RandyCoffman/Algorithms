def binary_search(list, item):
    first = 0
    last = len(list)-1 

    while first <= last:
        middle = round((first + last) / 2)
        guess = list[middle]
        print(guess)
        if guess == item:
            return middle
        if guess > item:
            last = middle - 1
        else:
             first = middle + 1
    return None

my_list = [1,2,3,4,5,6,7,8]

binary_search(my_list, 4)
