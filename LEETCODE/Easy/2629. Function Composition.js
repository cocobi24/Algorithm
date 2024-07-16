// https://leetcode.com/problems/function-composition/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {Function[]} functions
 * @return {Function}
 */
let compose = function(functions) {
    return function(x) {
        for (let i=1; i <= functions.length; i++) {
            let fn = functions[functions.length - i]
            x = fn(x)
            console.log(x)
        }
        return x
    }
};