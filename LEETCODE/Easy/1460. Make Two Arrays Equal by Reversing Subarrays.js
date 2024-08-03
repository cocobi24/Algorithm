// https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/?envType=daily-question&envId=2024-08-03

/**
 * @param {number[]} target
 * @param {number[]} arr
 * @return {boolean}
 */
let canBeEqual = function(target, arr) {
    let t = [...target].sort((a,b)=>{return a-b})
    let a = [...arr].sort((a,b)=>{return a-b})

    let answer = true;
    for(let i = 0; i < arr.length; i++){
        if (t[i] != a[i]) {
            answer = false;
            break
        }
    }
    return answer
    
};