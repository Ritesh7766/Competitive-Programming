#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        
        for (int i = 0; i < nums.size(); i++) {
            int required = target - nums[i];
            if (map.count(required) == 1)
                return vector<int>{map[required], i};
            map[nums[i]] = i;
        }
        return vector<int>();
    }
};