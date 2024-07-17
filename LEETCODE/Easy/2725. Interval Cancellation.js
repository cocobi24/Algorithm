// https://leetcode.com/problems/interval-cancellation/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
let cancellable = function(fn, args, t) {
    fn(...args)
    let interval = setInterval(() => {
        fn(...args)
    }, t);

    return function() {
        clearTimeout(interval);
    }
};