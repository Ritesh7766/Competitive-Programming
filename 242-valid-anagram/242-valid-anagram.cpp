#include <vector>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
            return false;
        vector<int> map(26, 0);
        
        for (int i = 0; i < s.length(); i++) {
            map[s[i] - 'a'] += 1;
            map[t[i] - 'a'] -= 1;
        }
        
        for (auto count : map)
            if (count != 0) 
                return false;
        
        return true;
    }
};