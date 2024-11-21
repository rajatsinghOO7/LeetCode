class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1 = sorted(nums1)

        n = len(nums1)
        if n%2!=0:
            return (nums1[n//2])
        else:
            return ((nums1[(n//2)-1]+nums1[n//2])/2)