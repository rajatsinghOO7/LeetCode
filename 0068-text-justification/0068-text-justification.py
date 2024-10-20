from typing import List

class Solution:
    
    def spaceadd(self, words, maxWidth, is_last_line):
        if is_last_line:
            return ' '.join(words) + ' ' * (maxWidth - len(' '.join(words)))
        total_chars = sum(len(word) for word in words)
        num_gaps = len(words) - 1
        
        if num_gaps == 0:
            return words[0] + ' ' * (maxWidth - len(words[0]))
        
        space_between_words = (maxWidth - total_chars) // num_gaps
        extra_spaces = (maxWidth - total_chars) % num_gaps
        
        result = ''
        for i in range(num_gaps):
            result += words[i] + ' ' * (space_between_words + (1 if i < extra_spaces else 0))
        
        result += words[-1]
        return result

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + len(current_line) > maxWidth:
                res.append(self.spaceadd(current_line, maxWidth, False))
                current_line = []
                current_length = 0
            current_line.append(word)
            current_length += len(word)
        
        res.append(self.spaceadd(current_line, maxWidth, True))
        
        return res
