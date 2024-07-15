# https://www.acmicpc.net/problem/1918

notation = input()
stack = []
answer = ''

for n in notation:
  if n.isalpha():
    answer += n
  else:
    if n == '(':
      stack.append(n)

    elif n in ['*', '/']:
      while stack and (stack[-1] in ['*', '/']):
        answer += stack.pop()
      stack.append(n)

    elif n in [')', '+', '-']:
      while stack and stack[-1] != '(':
        answer += stack.pop()
      if n == ')':
        stack.pop()
      else:
        stack.append(n)

print(answer, *stack[::-1], sep='')