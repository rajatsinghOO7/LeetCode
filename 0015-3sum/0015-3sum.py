class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums = sorted(nums)
        n = len(nums)

        for i in range(0,n):
            if (i>0 and nums[i] == nums[i-1]):
                continue

            j = i + 1
            k = n - 1
            while(j<k):
                sum1 = nums[i] + nums[j] + nums[k]
                if(sum1<0):
                    j += 1
                elif(sum1>0):
                    k -= 1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    ans.add(tuple(temp))
                    j += 1
                    k -= 1
        return list(ans)
