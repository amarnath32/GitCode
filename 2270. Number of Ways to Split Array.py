class Solution(object):
    def waysToSplitArray(self, nums):
        total = sum(nums)
        sums = [0]*len(nums)
        sums[0] =nums[0]
        count =0

        for i in range(1,len(nums)):
            sums[i] = sums[i-1]+nums[i]

        print(sums)

        for j in range(len(nums)-1):
            if sums[j] >= total -sums[j]:
                count+=1
        
        return count
        
        



a=Solution()
print(a.waysToSplitArray([10,4,-8,7])) #2
print(a.waysToSplitArray([2,3,1,0])) #1