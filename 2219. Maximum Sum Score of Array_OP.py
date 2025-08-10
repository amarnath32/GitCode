class Solution(object):
    def maximumSumScore(self, nums):
        total = sum(nums)
        max_sum = float('-inf')

        left_sum = nums[0]

        max_sum = max(nums[0],total)

        for i in range(1,len(nums)):
            left_sum+=nums[i]
            max_sum = max(max(left_sum,total-left_sum+nums[i]),max_sum)
        return max_sum
    
a=Solution()
print(a.maximumSumScore([4,3,-2,5])) #10
print(a.maximumSumScore([-3,-5 ])) #-3
print(a.maximumSumScore([-6,0,-2,-3]))
           