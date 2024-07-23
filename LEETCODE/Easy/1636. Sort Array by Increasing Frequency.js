// https://leetcode.com/problems/sort-array-by-increasing-frequency/description/?envType=daily-question&envId=2024-07-23

/**
 * @param {number[]} nums
 * @return {number[]}
 */
let frequencySort = function(nums) {
  let temp = [];
  let answer = [];
  for (let i = 0; i< nums.length; i++) {
    let idx = nums[i] < 0 ? (-nums[i] - 1) : nums[i] + 100;
    temp[idx] = !temp[idx] ? [nums[i] , 0] : temp[idx]
    temp[idx][1] += 1;
  }
  temp = temp.filter(row => row);
  temp.sort((a, b) => {
    if (a[1] === b[1]) {
    return b[0] - a[0]
    }
    return a[1] - b[1]
  });
  
  for (let i = 0; i < temp.length; i++) {
    for (let j = 0; j < temp[i][1]; j++) {
    answer.push(temp[i][0]);
    }
  }
  
  return answer
};