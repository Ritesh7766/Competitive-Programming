#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        if (p.length() > s.length())
            return vector<int>();
        
        vector<int> res, key(26, 0), map(26, 0);
        int matches = 0;
        
        for (char ch : p)
            key[ch - 'a'] += 1;
        
        for (int i = 0; i < p.length(); i++)
            map[s[i] - 'a'] += 1;
            
        for (int i = 0; i < 26; i++)
            if (map[i] == key[i])
                matches += 1;
        
        int l = 0;
        for (int r = p.length(); r < s.length(); r++) {
            if (matches == 26)
                res.push_back(l);
            matches = 0;
            map[s[r] - 'a'] += 1;
            map[s[l] - 'a'] -= 1;
            
            for (int i = 0; i < 26; i++)
                if (map[i] == key[i])
                    matches += 1;
                
            l += 1;
        }
        
        if (matches == 26)
            res.push_back(l);
        return res;
    }
};