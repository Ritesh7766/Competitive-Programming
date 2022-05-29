#include <unordered_set>
#include <queue>
#include <array>


using namespace std;

class Solution {
public:
    int bfs(int node, unordered_set<int> &visited, unordered_set<int> &hash_set) {
        queue<int> q;
        q.push(node);
        visited.insert(node);
        int ln = 0;
        
        while (!q.empty() ) {
            int u = q.front();
            q.pop();
            ln += 1;
            array<int, 2> adj_verts{u - 1, u + 1};
            for (int v : adj_verts) 
                if (hash_set.count(v) == 1 && visited.count(v) == 0) {
                    q.push(v);
                    visited.insert(v);
                }
        }
        return ln;
    }
    
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> visited, hash_set;
        
        for (int num : nums)
            hash_set.insert(num);
        
        int max_len = 0;
        for (int num : nums)
            if (visited.count(num) == 0)
                max_len = max(max_len, bfs(num, visited, hash_set) );
        
        return max_len;
    }
};