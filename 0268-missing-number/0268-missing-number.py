class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        addd = 0
        n = len(nums)+1
        sum1 = (n*(n+1))//2
        for i in nums:
            sum1 = sum1-i
        return sum1
        