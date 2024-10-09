// let nums = [10, 2]; // resutl = 210;
let nums = [11111111111121, 11111111111112]; // result = 9534330;

/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
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



let a = new largestNumber(nums)
console.log(a)
