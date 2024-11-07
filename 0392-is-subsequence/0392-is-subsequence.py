import re

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # If s is empty, it is always a subsequence of t
        if not s:
            return True
        
        # Use a regular expression with lookaheads to match each character of s in t
        pattern = '.*'.join(map(re.escape, s))  # Join the characters of s with '.*'
        
        # Look for the pattern in t
        return bool(re.search(pattern, t))  # Use search instead of fullmatch
