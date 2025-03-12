// https://neetcode.io/problems/duplicate-integer

class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const numSet = new Set(nums)
        return nums.length !== numSet.size
    }
}