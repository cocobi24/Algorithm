// https://neetcode.io/problems//top-k-elements-in-list

class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const numSet = {}
        for (let i = 0; i < nums.length; i++) {
            numSet[nums[i]] = 1 + (numSet[nums[i]] || 0)
        }

        const freqList = [[]]
        const keys = Object.keys(numSet)
        for (let i = 0; i < nums.length; i++) {
            freqList.push([])
        }

        for (let i = 0; i < keys.length; i++) {
            freqList[numSet[keys[i]]].push(keys[i]);
        }

        const ans = []
        for (let i = nums.length; i > 0; i--) {
            if (freqList[i].length === 0) {
                continue
            }

            for (let freq of freqList[i]) {
                ans.push(freq);
                if (ans.length === k) {
                    return ans
                }
            }
        }

    }
}
