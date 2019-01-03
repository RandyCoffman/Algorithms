def binary_search(list, item):
    low = list[0]
    high = len(list)-1
    middle = round((low + high) / 2)
    guess = list[middle]
    if guess == item:
        return item
    if guess > item:
        high = middle - 1
        print(high)
        binary_search(list[high], item)
    elif guess < item:
        low = middle + 1
        print(low)
        binary_search(list[low:], item)
    return None


my_list = [1,2,3,4,5,6,7,8]

print(binary_search(my_list, 4))
