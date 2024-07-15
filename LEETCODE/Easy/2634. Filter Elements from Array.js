// https://leetcode.com/problems/filter-elements-from-array/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
let filter = function(arr, fn) {
    let newArr = [];
    for(let i=0; i < arr.length; i++){
        let n = fn(arr[i], i)
        if ( n ){
            newArr.push(arr[i])
        }
    }
    return newArr
};