class Solution:

    def invert(self, S):
        return ''.join('1' if char == '0' else '0' for char in S)

    def findKthBit(self, n: int, k: int) -> str:
        if n < 1:
            return
        S = '0'
        for _ in range(2, n + 1):
            inverted = self.invert(S)
            S = S + '1' + inverted[::-1]
        return(S[k-1])