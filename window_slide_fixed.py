def max_sum_subarray(arr, k):
    n = len(arr)
    # Edge case: array is smaller than the window size
    if n < k:
        return None  

    # 1. Compute the sum of the first window of size k
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # 2. Slide the window from the k-th element to the end
    for i in range(k, n):
        # Add the new element entering the window, subtract the one leaving
        window_sum = window_sum + arr[i] - arr[i - k]
        
        # Update the maximum sum found so far
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage:
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))  # Output: 9 (from the subarray [5, 1, 3])
