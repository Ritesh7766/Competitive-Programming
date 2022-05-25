#include <unordered_set>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> exists;
        for (auto num : nums) {
            if (exists.count(num))
                return true;
            exists.insert(num);
        }
        return false;
    }
};