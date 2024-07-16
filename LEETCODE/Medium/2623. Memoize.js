// https://leetcode.com/problems/memoize/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let memo = {}
    return function(...args) {
        let s = String(args)
        if (memo[s] !== undefined) {
            return memo[s]
        }
        memo[s] = fn(...args)
        return memo[s]
    }
}