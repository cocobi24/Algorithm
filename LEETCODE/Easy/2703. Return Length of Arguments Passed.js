// https://leetcode.com/problems/return-length-of-arguments-passed/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
let argumentsLength = function(...args) {
    return args.length
};