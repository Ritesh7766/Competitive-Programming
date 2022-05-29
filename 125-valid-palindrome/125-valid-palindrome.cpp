#include <string>

class Solution {
public:
    bool isPalindrome(string s) {
        string wrd;
        for (char ch : s)
            if (isalpha(ch) || isdigit(ch) )
                wrd.push_back(tolower(ch) );
        
        string rev;
        for (int i = wrd.length() - 1; i >= 0; i--)
            rev.push_back(wrd[i]);
        return rev == wrd;
    }
};