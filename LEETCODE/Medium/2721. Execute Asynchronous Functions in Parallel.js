// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
let promiseAll = function(functions) {
    return new Promise((resolve,reject) => {
        const results = new Array(functions.length);
        let count = 0
        functions.forEach((fn,i) =>{
            fn().then(res=>{
                results[i]=res;
                count++;
                if(count===functions.length){
                    resolve(results);
                }
            }).catch(error=>reject(error))
        } )
    })
};