# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        close_dict = { ')': '(', '}' : '{', ']' : '[' }
        close_list = [ ')', '}', ']']

        s_len = len(s)
        if s_len == 1:
            return False
        elif s_len > 1:
            s_list = list(s)
            stack = [s_list[0]]
            for i in range(1, s_len):
                if s_list[i] in close_list:
                    if len(stack) == 0:
                        return False
                    if stack[-1] == close_dict[s_list[i]]:
                        stack.pop()
                    else:
                        break
                else:
                    stack.append(s_list[i])
                return True if len(stack) == 0 else False
