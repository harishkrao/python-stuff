class Solution:
    def twoSum(self, nums, target):
        for val in nums:
            for val2 in nums[nums.index(val)+1:]:
                if val2 == target - val:
                    print(val, val2, nums)
                    return nums.index(val), nums.index(val2, nums.index(val)+1)



s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))

print(s.twoSum([2, 5, 5, 11], 10))

