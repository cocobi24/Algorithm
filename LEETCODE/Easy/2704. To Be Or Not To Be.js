// https://leetcode.com/problems/to-be-or-not-to-be/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {string} val
 * @return {Object}
 */
let expect = function(val) {
    return {
        toBe: (n)=> {
            if (val === n) return true
            throw new Error("Not Equal")
        },
        notToBe: (n)=> {
            if (val !== n) return true
            throw new Error("Equal")
        },
    }
};