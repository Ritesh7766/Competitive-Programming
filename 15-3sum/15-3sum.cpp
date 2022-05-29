#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end() );
        
        vector<vector<int> > res; 
        for (int i = 0, n = nums.size(); i < n; i++) {
            if (i > 0 and nums[i - 1] == nums[i])
                continue;
            int left = i + 1, right = n - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    res.push_back(vector<int>{nums[i], nums[left], nums[right]});
                    left += 1;
                    while (left < right and nums[left] == nums[left - 1])
                        left += 1;
                }
                else if (sum > 0)
                    right -= 1;
                else
                    left += 1;
            }
        }
        return res;
    }
};