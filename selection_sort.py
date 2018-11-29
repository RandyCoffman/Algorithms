def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSortSmall(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

def findBiggest(arr):
    biggest = arr[0]
    biggest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]
            biggest_index = i
    return biggest_index

def selectionSortBig(arr):
    newArr = []
    for i in range(len(arr)):
        biggest = findBiggest(arr)
        newArr.append(arr.pop(biggest))
    return newArr

print(selectionSortSmall([100,50,20,12,70,7,45,78,3556,3453456,12,45,6,17,5,13,3,18,22,0]))
print(selectionSortBig([100,50,20,12,70,7,45,78,3556,3453456,12,45,6,17,5,13,3,18,22,0]))
