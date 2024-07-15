// https://leetcode.com/problems/array-reduce-transformation/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
let reduce = function(nums, fn, init) {
    if (nums.length != 0){
        let val = fn(init, nums[0]);
        for(let i = 1; i < nums.length; i++){
            val = fn(val, nums[i]);
        }
        return val;
        }
    return init;  
};