// https://neetcode.io/problems/is-anagram

class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const lenS = s.length;
        if (lenS !== t.length) {
            return false
        }

        const arr = new Array(26).fill(0);
        for (let i=0; i < lenS; i++) {
            arr[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
            arr[t.charCodeAt(i) - 'a'.charCodeAt(0)]--;
        }

        return arr.every(num => num === 0)
    }
}
