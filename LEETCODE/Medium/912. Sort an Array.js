// https://leetcode.com/problems/sort-an-array/description/?envType=daily-question&envId=2024-07-25

/**
 * @param {number[]} nums
 * @return {number[]}
 */
let sortArray = function(nums) {
  if (nums.length <= 1) return nums;
  const mid = Math.floor(nums.length / 2);
  const left = sortArray(nums.slice(0, mid));
  const right = sortArray(nums.slice(mid));
  
  return merge(left, right);
  };
  
  let merge = (arr1, arr2) => {
  const results = [];
  let i = 0;
  let j = 0;
  
  while (i < arr1.length && j < arr2.length) {
    if (arr2[j] > arr1[i]) {
    results.push(arr1[i]);
    i++;
    } else {
    results.push(arr2[j]);
    j++;
    }
  }
  
  while (i < arr1.length) {
    results.push(arr1[i]);
    i++;
  }
  
  while (j < arr2.length) {
    results.push(arr2[j]);
    j++;
  }
  
  return results;
}