class Solution(object):
    def searchInsert(self, nums, target):   
        n=len(nums)
        if target > nums[-1]:
            return n
        if target <nums[0]:
            return 0

        nums1 = nums
        mid = len(nums1)
        result =0
        n = len(nums)
        while mid>1:
            mid = int(len(nums1)/2)
            if target < nums1[mid]:
                nums1 = nums1[:mid]
            else:
                nums1 = nums1[mid:]

        return (nums.index(nums1[0])) if nums1[0] >= target else (nums.index(nums1[0])+1)




a =Solution()
print(a.searchInsert([1,3,5,6],7))

        