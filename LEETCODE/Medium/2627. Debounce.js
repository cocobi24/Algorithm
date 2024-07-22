// https://leetcode.com/problems/debounce/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
let debounce = function(fn, t) {
    let timeoutId;
    return function(...args) {
        clearTimeout(timeoutId);
            timeoutId = setTimeout(() => {
                fn.apply(this, args);
        }, t);
    }
};