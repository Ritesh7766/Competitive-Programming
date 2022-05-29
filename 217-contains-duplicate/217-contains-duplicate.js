/**
 * @param {number[]} nums
 * @return {boolean}
 */

var containsDuplicate = function(nums) {
    var hash_set = new Set();
    for (var i in nums) {
        if (hash_set.has(nums[i]) ) 
            return true;
        hash_set.add(nums[i]);
    }
    return false;
};