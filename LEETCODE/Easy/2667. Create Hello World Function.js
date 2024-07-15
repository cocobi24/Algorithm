// https://leetcode.com/problems/create-hello-world-function/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @return {Function}
 */
let createHelloWorld = function() {
    function f() {
        return "Hello World"
    }
    return f
};
const f = createHelloWorld();
console.log(f());