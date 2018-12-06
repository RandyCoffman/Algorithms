def array_len(arr, count):
    if not arr:
        return 0
    else:
        del arr[0]
        count = count + array_len(arr,count)
    return count



arr = [1,2,3,4,5,6,7,8,9,10,11,12]
# arr = []
print(array_len(arr,1))

# def count(list):
#  if list == []:
#     return 0
#  return 1 + count(list[1:])