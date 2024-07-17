// https://leetcode.com/problems/add-two-promises/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
let addTwoPromises = async function(promise1, promise2) {
    return Promise.all([promise1, promise2])
        .then((res) => {
            return res[0] + res[1]
        })

};