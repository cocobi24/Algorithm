# https://neetcode.io/problems/duplicate-integer

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = set()
        ans = False
        for n in nums:
            if n not in dic:
                dic.add(n)
            else:
                ans = True
                break
        return ans