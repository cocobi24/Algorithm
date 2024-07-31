# https://www.acmicpc.net/problem/29812

N = int(input())
S = list(input().rstrip())
D, M = map(int, input().split())
HYU_set = {'H': 0, 'Y': 0, 'U': 0}
HYU = ['H', 'Y', 'U']

stack = []
energe = 0
for _ in range(N):
  s = S.pop()
  if s in HYU:
    HYU_set[s] += 1
    if len(stack) > 0:
      energe += min(len(stack) * D, M + D)
      stack.clear()
  else:
    stack.append(s)

energe += min(len(stack) * D, M + D)
min_cnt = min(HYU_set.values())
print(energe if energe > 0 else "Nalmeok")
print(min_cnt if min_cnt else "I love HanYang University")