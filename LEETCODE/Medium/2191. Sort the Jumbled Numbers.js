// https://leetcode.com/problems/sort-the-jumbled-numbers/description/?envType=daily-question&envId=2024-07-24

let sortJumbled = function(mapping, nums) {
  let dict = {};
  for (let i = 0; i < mapping.length; i++) {
    dict[`${i}`] = mapping[i];
  }

  let len = nums.length;
  let str = '', newNum = '';
  let sortedArr = []
  for (let i = 0; i < len; i++) {
    str = String(nums[i]).split('');
    newNum = '';
    for (let j = 0; j < str.length; j++) {
      newNum += dict[str[j]];
    }
    newNum = parseInt(newNum);
    sortedArr.push([i, newNum, nums[i]]);
  }

  sortedArr.sort((a, b) => {
    if (a[1] !== b[1]) {
      return a[1] - b[1]
    }
    return a[0] - b[0]
  });
  sortedArr = sortedArr.map(n => n[2]);
  console.log(sortedArr)
  return sortedArr
};