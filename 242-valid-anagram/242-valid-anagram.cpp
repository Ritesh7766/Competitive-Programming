#include <unordered_map>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
            return false;
        unordered_map<char, int> map;
        
        for (int i = 0; i < s.length(); i++) {
            if (!map.count(s[i]))
                map[s[i]] = 0;
            if (!map.count(s[i]))
                map[t[i]] = 0;
            map[s[i]] += 1;
            map[t[i]] -= 1;
        }
        
        for (auto item : map)
            if (item.second != 0)
                return false;
        
        return true;
    }
};