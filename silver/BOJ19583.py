# https://www.acmicpc.net/problem/19583

import sys
input = sys.stdin
S, E, O = map(str, input.readline().split())
S = int(S[:2] + S[3:])
E = int(E[:2] + E[3:])
O = int(O[:2] + O[3:])

chat = set()
cnt = 0
for s in input:
  time, nick = map(str, s.rstrip().split())
  time = int(time[:2] + time[3:])
  if time <= S:
    chat.add(nick)
  elif E <= time <= O and nick in chat:
    chat.remove(nick)
    cnt += 1
print(cnt)