// https://leetcode.com/problems/kth-largest-element-in-a-stream/description/?envType=daily-question&envId=2024-08-12

/**
 * @param {number} k
 * @param {number[]} nums
 */
let KthLargest = function(k, nums) {
    this.arr = nums.sort((a, b) => a - b);
    this.k = k;
};

/** 
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function(val) {
    this.arr.push(val);
    this.arr.sort((a, b) => a - b);
    let len = this.arr.length;
    return this.arr[len - this.k]
};