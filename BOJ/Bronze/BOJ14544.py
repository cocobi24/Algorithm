# https://www.acmicpc.net/problem/14544

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
  N, K = map(int, input().split())
  person = {input().rstrip(): 0 for _ in range(N)}
  for _ in range(K):
    name, cnt, _ = map(str, input().split())
    person[name] += int(cnt)

  votes = list(person.values())
  person = list(person.items())
  person.sort(key=lambda x: -x[1])

  if votes.count(person[0][1]) == 1:
    print(f'VOTE {i+1}: THE WINNER IS {person[0][0]} {person[0][1]}')
  else:
    print(f'VOTE {i+1}: THERE IS A DILEMMA')