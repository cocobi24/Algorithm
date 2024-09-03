// https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/?envType=daily-question&envId=2024-09-03

let alphaDict = {};
for(let i = 97; i <= 122; i++){
  alphaDict[String.fromCharCode(i)] = (i - 96).toString();
}

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
let getLucky = function(s, k) {
  let sList = s.split('');
  let res = [];
  let len = sList.length;

  for (let i = 0; i < len; i++) {
    res.push(alphaDict[sList[i]]);
  }

  let total = 0;
  for (let i = 0; i < k; i++) {
    len = res.length;
    for (let j = 0; j < len; j++) {
      res[j] = res[j].split('');
      for (let k = 0; k < res[j].length; k++) {
        total += Number(res[j][k]);
      }
    }
    res = total.toString().split('');
    total = 0;
  }
  return res.join('')
};