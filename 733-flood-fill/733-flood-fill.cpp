#include <vector>

using namespace std;

class Solution {
public:
    vector<pair<int, int> > get_adjacent_vertices(const int rows, const int cols, pair<int, int> u) {
        vector<pair<int, int> > dirs{make_pair(1, 0), make_pair(0, 1), make_pair(-1, 0), make_pair(0, -1)};
        vector<pair<int, int> > adjacent_vertices;
        for (pair<int, int> dir : dirs) {
            int x = dir.first + u.first;
            int y = dir.second + u.second;
            if (0 <= x && x < rows && 0 <= y && y < cols) 
                adjacent_vertices.push_back(make_pair(x, y) ); 
        }
        return adjacent_vertices;
    }
    
    void dfs(vector<vector<int>>& image, pair<int, int> u, int newColor, int initial_color) {
        image[u.first][u.second] = newColor;
        vector<pair<int, int> > adjacent_vertices = get_adjacent_vertices(image.size(), image[0].size(), u);
        for (pair<int, int> v : adjacent_vertices) 
            if (image[v.first][v.second] == initial_color)
                dfs(image, v, newColor, initial_color);
        return;
    }
    
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        if (image[sr][sc] == newColor)
            return image;
        int initial_color = image[sr][sc];
        dfs(image, make_pair(sr, sc), newColor, initial_color);
        return image;
    }
};