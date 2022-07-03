class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        map, alpha = {' ' : ' '}, 97
        for ch in key:
            if ch in map or ch == ' ':
                continue
            map[ch] = chr(alpha)
            alpha += 1
        decoded_msg = ''
        for ch in message:
            decoded_msg += map[ch]
        return decoded_msg