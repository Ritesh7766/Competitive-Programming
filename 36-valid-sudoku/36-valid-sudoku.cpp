#include <vector>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<int> > row_mp;
        unordered_map<int, unordered_set<int> > col_mp;
        map<pair<int, int>, unordered_set<int> > grd_mp;
        
        const int N = 9;
        
        for (int i = 0, n = N / 3; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (row_mp.count(i) == 0)
                    row_mp[i] = unordered_set<int>();
                if (col_mp.count(j) == 0)
                    col_mp[i] = unordered_set<int>();
                grd_mp[make_pair(i, j)] = unordered_set<int>();
            }
        }
        
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == '.') 
                    continue;
                
                if (row_mp[i].count(board[i][j]) == 1)
                    return false;
                if (col_mp[j].count(board[i][j]) == 1)
                    return false;
                if (grd_mp[make_pair(i / 3, j / 3)].count(board[i][j]) == 1)
                    return false;
                
                row_mp[i].insert(board[i][j]);
                col_mp[j].insert(board[i][j]);
                grd_mp[make_pair(i / 3, j / 3)].insert(board[i][j]);
            }
        }
        
        return true;
    }
};