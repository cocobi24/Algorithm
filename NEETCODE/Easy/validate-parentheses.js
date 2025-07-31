// https://neetcode.io/problems/validate-parentheses

class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = [];
        const closeSet = { ")": "(", "]": "[", "}": "{" }
        
        for (let i = 0; i < s.length; i++) {
            const char = s[i];
            if (char in closeSet) {
                if (stack.length === 0 || stack.pop() !== closeSet[char]) {
                    return false;
                }
            } else {
                stack.push(char);
            }
        }
        return stack.length === 0;
    }
}