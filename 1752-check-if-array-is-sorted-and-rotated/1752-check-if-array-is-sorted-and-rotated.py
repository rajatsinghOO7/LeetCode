class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0 
        for i in range(0, len(nums)-1):
            if nums[i+1]<nums[i]:
                count+=1
        print(count)
        if nums[0]<nums[len(nums)-1]:
            count+=1
        if count<=1:
            return True
        return False