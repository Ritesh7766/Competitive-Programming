/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (t.length != s.length)
        return false;
    var key = new Array(26).fill(0);
    for (var i in s) {
        key[t.charCodeAt(i) - 'a'.charCodeAt()] += 1;
        key[s.charCodeAt(i) - 'a'.charCodeAt()] -= 1;
    }
 
    for (var i in key) 
        if (key[i] != 0)
            return false;
    
    return true;
};