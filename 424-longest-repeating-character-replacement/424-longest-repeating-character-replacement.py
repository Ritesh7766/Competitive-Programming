class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = [0] * 26
        
        left, mx_len = 0, 0
        for right in range(len(s)):
            char_map[ord(s[right]) - ord('A')] += 1
            while (right - left + 1) - max(char_map) > k:
                char_map[ord(s[left]) - ord('A')] -= 1
                left += 1
            mx_len = max(mx_len, right - left + 1)
        return mx_len