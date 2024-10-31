from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start: int, path: List[int]):
            result.append(path.copy())  # Add the current subset to the result
            for i in range(start, len(nums)):
                path.append(nums[i])  # Include nums[i] in the current subset
                backtrack(i + 1, path)  # Move on to the next element
                path.pop()  # Backtrack to explore other subsets
        
        backtrack(0, [])
        return result
