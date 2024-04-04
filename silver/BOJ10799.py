# https://www.acmicpc.net/problem/10799

stick = list(input().rstrip())
stack = []
cnt = 0
for i in range(len(stick)):
  if stick[i] == '(':
    stack.append(stick[i])
  else:
    if stick[i-1] == '(':
      stack.pop()
      cnt += len(stack)
    else:
      stack.pop()
      cnt += 1
print(cnt)