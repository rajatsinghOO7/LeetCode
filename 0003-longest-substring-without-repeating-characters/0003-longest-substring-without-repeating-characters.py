class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxsum = 0
        currentsum = 1
        for i in range (0,len(s)-1):
            if ord(s[i]) == ord(s[i+1])-1:
                currentsum += 1
            else:
                currentsum = 1
            maxsum = max(maxsum, currentsum)
        return maxsum


        