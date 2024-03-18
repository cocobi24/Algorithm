# https://www.acmicpc.net/problem/12756

aa, al = map(int, input().split())
ba, bl = map(int, input().split())
while al > 0 and bl > 0:
  al -= ba
  bl -= aa

if al > 0:
  print("PLAYER A")
elif bl > 0:
  print("PLAYER B")
else:
  print("DRAW")