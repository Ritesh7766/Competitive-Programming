from math import inf

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        mp = collections.defaultdict(int)
        for i, msg in enumerate(messages):
            mp[senders[i]] += len(msg.split(' ') )
        
        mx_cnt = max(mp.values() )
        
        return max([user for user, cnt in mp.items() if cnt == mx_cnt])