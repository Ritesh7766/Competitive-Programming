class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [ch.lower() for ch in s if ch.isalnum()]
        return tuple(chars) == tuple(chars[::-1])