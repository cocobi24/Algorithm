// https://leetcode.com/problems/promise-time-limit/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
let timeLimit = function(fn, t) {
    return async function(...args) {
        const promise = [
            new Promise(resolve => resolve(fn(...args))), 
            new Promise((resolve, reject) => setTimeout(
                () => reject('Time Limit Exceeded'), t)) 
            ] 
        return Promise.race(promise);
    }
};