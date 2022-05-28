#include <vector>
#include <string>
#include <array>
#include <map>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<array<int, 26>, vector<string>> anagram_grp;
        for (string str : strs) {
            array<int, 26> key{0};
            for (char ch : str)
                key[ch - 'a'] += 1;
            anagram_grp[key].push_back(str);
        }
        
        vector<vector<string>> res;
        
        for (auto pair : anagram_grp)
            res.push_back(pair.second);
        return res;
    }
};