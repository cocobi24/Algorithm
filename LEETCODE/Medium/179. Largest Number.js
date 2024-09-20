// https://leetcode.com/problems/largest-number/description/?envType=daily-question&envId=2024-09-18

/**
 * @param {number[]} nums
 * @return {string}
 */
const largestNumber = function(nums) {
  nums = nums.map(num => num.toString());
  nums.sort((a, b) => {
    if (a + b > b + a) {
      return -1;
    } else if (a + b < b + a) {
      return 1;
    }
    return 0;
  });

  let result = nums.join('');
  return Number(result) == 0 ? '0' : result;
};