#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Allocate memory.
        vector<int>* buckets = new vector<int>[nums.size() + 1];
        vector<int> result;
        unordered_map<int, int> frequency;
        
        for (int num : nums) {
            if (frequency.count(num) == 0)
                frequency[num] = 0;
            frequency[num] += 1;
        }
        
        
        for (auto pair : frequency) 
           buckets[pair.second].push_back(pair.first);
      
        
        for (int i = nums.size(); i >= 0; i--) {
            if (k <= 0) break;
            k -= (buckets[i].size() );
            for (int num : buckets[i])
                result.push_back(num);
        }
        
        // Deallocate memory (Leetcode won't let me do it. Not sure why?)
        // delete buckets;*/
        
        return result;
    }
};