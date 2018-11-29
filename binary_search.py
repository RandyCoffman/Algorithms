def binary_search(list, item):
    start = 0
    stop = len(list)-1 

    while start <= stop:
        middle = round((start + stop) / 2)
        guess = list[middle]
        print(guess)
        if guess == item:
            return middle
        if guess > item:
            stop = middle - 1
        else:
             start = middle + 1
    return None

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

binary_search(my_list, 4)
