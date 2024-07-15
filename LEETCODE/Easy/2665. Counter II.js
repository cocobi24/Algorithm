// https://leetcode.com/problems/counter-ii/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
let createCounter = function(init) {
    let n = init;
    return {
        reset: () =>{
            n = init;
            return n
        },
        increment: ()=>{
            n += 1;
            return n
        },
        decrement: ()=>{
            n -= 1;
            return n
        }
    }
};

const counter = createCounter(5)
console.log(counter.increment()); // 6
console.log(counter.reset()); // 5
console.log(counter.decrement()); // 4