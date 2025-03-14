# https://neetcode.io/problems/is-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = sorted(s)
        t_list = sorted(t)

        if len(s) != len(t):
            return False
        
        return s_list == t_list