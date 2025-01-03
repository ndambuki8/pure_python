#Dynamic programming - Longest increasing subsequence
def length_of_list(nums):
    dp = [1] * len(nums)
    print(dp)
    for i in range(len(nums)):
        for j in range(i):
            print(f"{nums[i]} > {nums[j]}")
            if nums[i] > nums[j]:
                print("dp bafore:", dp)
                dp[i] = max(dp[i], dp[j] + 1)
                print("dp afteri:", dp)
                print("DPI at i:",dp[i])
    return max(dp)

# Test
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print("Length of LIS:", length_of_list(nums))     