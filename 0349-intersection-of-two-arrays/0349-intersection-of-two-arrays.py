class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0 
        j = 0
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        ans= set()
        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i] < nums2[j]):
                i+=1
            elif(nums2[j] < nums1[i]):
                j+=1
            else:
                ans.add(nums1[i])
                i+=1
                j+=1
        return ans