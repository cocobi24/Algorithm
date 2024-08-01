// https://leetcode.com/problems/number-of-senior-citizens/description/?envType=daily-question&envId=2024-08-01

/**
 * @param {string[]} details
 * @return {number}
 */
let countSeniors = function(details) {
    let cnt = 0;
    for (let i=0; i < details.length; i++) {
        if (details[i].length === 15) {
            let age = Number(details[i].slice(11, 13));
            if (age > 60) {
                cnt++;
            }
        }
    }
    return cnt
};