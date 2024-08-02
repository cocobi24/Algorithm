# https://www.acmicpc.net/problem/31562

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

octave_set = {}
for _ in range(N):
  song = list(input().rstrip().split())
  octave = song[2] + song[3] + song[4]
  if octave in octave_set:
    octave_set[octave][0].add(song[1])
    octave_set[octave][1] += 1
  else:
    octave_set[octave] = [{song[1]}, 1]

for _ in range(M):
  target = str(input().rstrip()).replace(' ', '')
  if target in octave_set:
    print(*octave_set[target][0] if octave_set[target][1] == 1 else '?')
  else:
    print('!')