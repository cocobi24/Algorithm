# https://www.acmicpc.net/problem/1935

n = int(input())
fomula = input()
nums = [int(input()) for _ in range(n)]

def postfix_notation(fomula) :
    stack = []
    for s in fomula :
        if s == '+' or s == '-' or s == '*' or s == '/' :
            b = stack.pop()
            a = stack.pop()
            if s == '+' :
                stack.append(a + b)
            elif  s == '-' :
                stack.append(a - b)
            elif s == '*':
                stack.append(a * b)
            elif s == '/':
                stack.append(a / b)
        else :
            stack.append(nums[ord(s)-ord('A')])
    return stack[0]

answer = postfix_notation(fomula)
print(format(answer, '.2f'), end='')