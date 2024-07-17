// https://leetcode.com/problems/sleep/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    return new Promise((res, rej) => {
        setTimeout(() => {
            res();
        }, millis)
    })
}