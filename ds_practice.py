class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n-1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

nums = [3,2,4]
target = 6
sol = Solution()

sol = sol.twoSum(nums, target)

print(sol)