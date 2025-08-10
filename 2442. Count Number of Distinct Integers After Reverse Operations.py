class Solution(object):
    def countDistinctIntegers(self, nums):

        seen = set(nums)
        
        def reverse(num):
            rev =0
            while num>0:
                rev = rev*10+num%10
                num//=10
            return rev
        
    
        for i in nums:
            seen.add(reverse(i))
        
        return len(seen)

# Time complexity: O(n)
a=Solution()
print(a.countDistinctIntegers([1,13,10,12,31])) # 6
print(a.countDistinctIntegers([1,1,1,1,1])) # 1
print(a.countDistinctIntegers([1,2,3,4,5])) # 5
print(a.countDistinctIntegers([2,2,2])) # 1