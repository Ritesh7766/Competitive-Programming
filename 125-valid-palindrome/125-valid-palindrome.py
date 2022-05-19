class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [ch.lower() for ch in s if ch.isalnum()]
        wrd = ''
        for ch in chars: wrd += ch
        return wrd == wrd[::-1]