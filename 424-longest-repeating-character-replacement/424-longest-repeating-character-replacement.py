class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = [0] * 26
        
        left, n = 0, len(s)
        mx_len = 0
        
        for right in range(n):
            char_freq[ord(s[right]) - ord('A')] += 1
            while (right - left + 1) - max(char_freq) > k:
                char_freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            mx_len = max(mx_len, right - left + 1)
        
        return mx_len