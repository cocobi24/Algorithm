// https://leetcode.com/problems/apply-transform-over-each-element-in-array/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
let map = function(arr, fn) {
    let newArr = []
    for(let i=0; i<arr.length; i++){
        newArr.push(fn(arr[i], i))
    }
    return newArr;
};