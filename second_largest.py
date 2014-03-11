list_o_numbers = [3,7,14,6,10,11]
list2 = [0,2]
list3 = [2, 2, 2, 2, 2]

def second_largest(numbers):
    largest = numbers[0]
    second_largest = None
    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] > second_largest:
            second_largest = numbers[i]
    if second_largest is not None:
        return second_largest


print second_largest(list_o_numbers)
print second_largest(list2)
print second_largest(list3)