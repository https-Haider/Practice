def second_max(numbers):
    max1=0
    max2=0
    for i in range(len(numbers)):
        if numbers[i]>max1:
            max1,max2=numbers[i],max1
        elif numbers[i]>max2 and numbers[i]!=max1:
            max2=numbers[i]
    return max1,max2

print(second_max([1, 2, 3, 4, 5]))
