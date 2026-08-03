def perf_sq(number):
    if number < 0:
        return "Negative numbers cannot be perfect squares."
    if number in (0,1):
        return True
    l=0
    r= number
    while l <= r:
        mid = (l + r) // 2
        if mid * mid == number:
            return mid
        elif mid * mid < number:
            l = mid + 1
        else:
            r = mid - 1
    return "Not a perfect square"


print(perf_sq(164))