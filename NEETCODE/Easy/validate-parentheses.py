# https://neetcode.io/problems/validate-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeSet = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }

        for i in s:
            if i in closeSet:
                if stack and stack[-1] == closeSet[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if len(stack) == 0 else False