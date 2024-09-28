class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentmax = 0
        maximum = 0
        for i in range(0,len(nums)):
            if(nums[i]==1):
                currentmax+=1
            else:
                currentmax = 0
            maximum = max(currentmax,maximum)
        return maximum