array = [1, 3, 5, 7, 8]
target = 15

def two_sum(array, target):
    l = 0
    r = len(array) - 1
    while l < r:
        s = array[l] + array[r]
        if s == target:
            return [l, r]
        elif s < target:
            l += 1
        else:
            r -= 1


result = two_sum(array, target)
print(result)

