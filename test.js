let nums = [7,7,7,7]
/**
 * @param {number[]} nums
 * @return {number[]}
 */
let smallerNumbersThanCurrent = function(nums) {
    let unique = [...new Set(nums)].sort((a, b) => b-a)
    let sort_nums = [...nums].sort((a, b) => b-a);

    let len = nums.length;
    let rank = {};
    for (let i=0; i < unique.length; i++ ) {
        rank[unique[i]] = len - sort_nums.lastIndexOf(unique[i]) - 1;
    }

    let ans = [];
    for (let i=0; i < len; i++ ) {
        ans.push(rank[String(nums[i])]);
    }

    return ans
};

let a = smallerNumbersThanCurrent(nums)
console.log(a)