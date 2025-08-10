class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        current_sum = 0
        prefix_sums = {0: 1}

        for num in nums:
            current_sum += num
            if current_sum - k in prefix_sums:
                count += prefix_sums[current_sum - k]
            if current_sum in prefix_sums:
                prefix_sums[current_sum] += 1
            else:
                prefix_sums[current_sum] = 1

        print(prefix_sums)

        return count
    
a=Solution()
print(a.subarraySum([1,1,1],2))
print(a.subarraySum([3,4,7,2,-3,1,4,2],7))
print(a.subarraySum([1,2,3],3))
        