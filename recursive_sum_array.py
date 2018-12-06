def sum_array(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        first_num = arr[0]
        del arr[0]
        sum = first_num + sum_array(arr)
    print(sum)
    return sum

my_list = [1,2,3,4,5]
print(sum_array(my_list))