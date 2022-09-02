#include <vector>

using namespace std;

class Solution {
public:
    void dfs(vector<vector<int> >& image, vector<pair<int, int> > dir, pair<int, int> u, int init_color, int color) {
        image[u.first][u.second] = color;
        for (pair<int, int> v : dir) {
            int x = v.first + u.first, y = v.second + u.second;
            if (0 <= x && x < image.size() && 0 <= y && y < image[0].size() && image[x][y] == init_color)
                dfs(image, dir, make_pair(x, y), init_color, color);
        }
        return;
    }
    
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        if (image[sr][sc] == color) return image;
        int rows = image.size(), cols = image[0].size();
        vector<pair<int, int> > dir{make_pair(0, 1), make_pair(0, -1), make_pair(1, 0), make_pair(-1, 0)};
        int initial_color = image[sr][sc];
        dfs(image, dir, make_pair(sr, sc), initial_color, color);
        return image;
    }
};