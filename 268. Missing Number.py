class Solution(object):
    def missingNumber(self, nums):
        
        n = len(nums)
        total = int((n*(n+1))//2)
        print(total)
        sum =0
        for num in nums:
            sum+=num

        return total -sum

a = Solution()
print(a.missingNumber([0,1]))
