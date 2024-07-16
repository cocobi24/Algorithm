// https://leetcode.com/problems/allow-one-function-call/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {Function} fn
 * @return {Function}
 */
let once = function(fn) {
    let count = 0
    return function(...args){
        if (count >= 1 ) {
            return undefined
        }
        count += 1
        let obj = [...args]
        let answer = fn(...obj)
        return answer
    }
};