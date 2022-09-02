/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, color) {
    if (image[sr][sc] === color) return image;
    var rows = image.length;
    var cols = image[0].length;
    var dir = [[0, -1], [0, 1], [1, 0], [-1, 0]];
    var initial_color = image[sr][sc];

    var dfs = function(u) {
        image[u[0]][u[1]] = color;
        for (var i = 0; i < dir.length; i++) {
            var x = dir[i][0] + u[0];
            var y = dir[i][1] + u[1];
            if (0 <= x && x < rows && 0 <= y && y < cols && image[x][y] === initial_color)
                dfs([x, y] );
        }
    };
    
    dfs([sr, sc] );
    return image;
};