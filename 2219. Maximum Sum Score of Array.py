class Solution(object):
    def maximumSumScore(self, nums):
        total = sum(nums)
        sums = [0]*len(nums)
        sums[0] =nums[0]
        max_sum = float('-inf')

        for i in range(1,len(nums)):
            sums[i] = sums[i-1]+nums[i]

        max_sum = max(max_sum,nums[0])

        for i in range(1,len(nums)):
            max_sum = max(max(sums[i],total-sums[i-1]),max_sum)

        return max_sum
    
a=Solution()
print(a.maximumSumScore([4,3,-2,5])) #10
print(a.maximumSumScore([-3,-5 ])) #-3
print(a.maximumSumScore([-6,0,-2,-3]))
           