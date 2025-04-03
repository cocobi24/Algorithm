# https://neetcode.io/problems//top-k-elements-in-list

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numSet = {}
        for num in nums:
            if num in numSet:
                numSet[num] += 1
            else:
                numSet[num] = 1

        freq = sorted(numSet.items(), key=lambda x: -x[1])
        ans = [freq[i][0] for i in range(k)]
        return ans
        