# https://www.acmicpc.net/problem/11586

import sys
input = sys.stdin.readline

N = int(input())
mirror_list = [ list(input().rstrip()) for _ in range(N)]
# 1 == 그대로, 2 == 좌우반전, 3 == 상하반전
K = int(input())

for i in range(N):
  if K == 1:
    print(''.join(mirror_list[i]))
  elif K == 2:
    print(''.join(mirror_list[i][::-1]))
  elif K == 3:
    if i == 0 :
      mirror_list.reverse()
    print(''.join(mirror_list[i]))