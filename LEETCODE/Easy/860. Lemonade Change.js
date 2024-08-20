// https://leetcode.com/problems/lemonade-change/description/?envType=daily-question&envId=2024-08-15

/**
 * @param {number[]} bills
 * @return {boolean}
 */
let lemonadeChange = function(bills) {
    const money = [0, 0, 0];
    const len = bills.length;
    let answer = true;
    for (let i = 0; i < len; i++) {
        if (bills[i] === 5) {
            money[0] += 1;
        } else if (bills[i] === 10) {
            if (money[0] > 0) {
                money[0] -= 1;
                money[1] += 1;
            } else {
                answer = false;
                break;
            }
        } else {
            if (money[0] > 0 && money[1] > 0) {
                money[0] -= 1;
                money[1] -= 1;
            } else if (money[0] >= 3) {
                money[0] -= 3;
            } else {
                answer = false;
                break;
            }
        }
    }
    return answer  
};