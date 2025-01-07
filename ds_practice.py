class Solution:
    def twoSum(self, nums, target):
        numMap = {}
        n = len(nums)

        #Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        #Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return[]

nums = [3,2,4]
target = 6
sol = Solution()

sol = sol.twoSum(nums, target)

print(sol)