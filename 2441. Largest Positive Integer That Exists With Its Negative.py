class Solution(object):
    def findMaxK(self, nums):
        max =0
        seen = set(nums)
        
        for i in nums:
            if -i in seen:
                if i > max:
                    max = i
         
        return max if max !=0 else -1



a=Solution()
print(a.findMaxK([-1,2,-3,3])) #3
print(a.findMaxK([1,2,3,4])) #-1
print(a.findMaxK([-1,10,6,7,-7,1])) #3
print(a.findMaxK([-10,8,6,7,-2,-3])) #-1