// https://neetcode.io/problems/length-of-last-word/question

class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLastWord(s) {
        const s_list = s.trim().split(' ')
        const len = s_list.length
        return s_list[len-1].length
    }
}