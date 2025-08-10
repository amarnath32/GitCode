class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        sums = [0]*len(nums)
        sums[0] =nums[0]
        count =0

        for i in range(1,len(nums)):
            sums[i] = sums[i-1]+nums[i]
            
        print(sums)

        if total - sums[0] == 0:
            return 0
        
        for j in range(len(nums)-1):
            if sums[j] == total -sums[j+1]:
                return j+1
        
        return -1
        

a=Solution()
print(a.pivotIndex([1,7,3,6,5,6])) #3
print(a.pivotIndex([1,2,3])) #-1
print(a.pivotIndex([2,1,-1])) #0
        
      