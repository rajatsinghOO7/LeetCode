class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_list = s1.split()
        s2_list = s2.split()
        set1 = set()
        
        for i in s2_list:
            if i not in s1_list:
                set1.add(i)
        return list(set1)