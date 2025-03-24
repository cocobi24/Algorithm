# https://neetcode.io/problems/anagram-groups

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for sts in strs:
            s = ''.join(sorted(sts))
            if s not in groups:
                groups[s] = [sts]
            else:
                groups[s].append(sts)

        ans = []
        for k, v in groups.items():
            ans.append(v)
        return ans
        