class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l =len(nums)
        d = {}
        for i,x in enumerate (nums):
            t = target - x
            if t in d:
                return [d[t],i]
            d[x] = i