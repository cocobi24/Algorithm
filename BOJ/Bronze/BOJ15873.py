# https://www.acmicpc.net/problem/15873

n = input()
answer = 0
if len(n) >= 3:
  answer = int(n[0]) + int(int(n[1::])) if n[1] != '0' else int(n[:2]) + int(n[2::])
else:
  answer = int(n[0]) + int(n[1])
print(answer)