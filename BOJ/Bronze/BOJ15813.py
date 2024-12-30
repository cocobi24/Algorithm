# https://www.acmicpc.net/problem/15813

n = int(input())

def get_name_score(s):
  return ord(s)-64

name = input().rstrip()
names = list(name)

score = 0
for n in names:
  score += get_name_score(n)
print(score)