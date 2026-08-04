def product_of_array_except_itself(nums):
    n=len(nums)
    prefix=[1]*n
    suffix=[1]*n
    answer=[1]*n

    for i in range(1,n):
        prefix[i]=prefix[i-1]*nums[i-1]

    for i in range(n-2,-1,-1):
        suffix[i]=suffix[i+1]*nums[i+1]

    for i in range(n):
        answer[i]=prefix[i]*suffix[i]

    return answer

nums=[1,2,3,4]
print(product_of_array_except_itself(nums))