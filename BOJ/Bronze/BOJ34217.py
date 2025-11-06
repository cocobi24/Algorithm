# https://www.acmicpc.net/problem/34217

a, b = map(int, input().split())
c, d = map(int, input().split())
ac = a + c
bd = b + d
if ac < bd:
  print("Hanyang Univ.")
elif ac > bd:
  print("Yongdap")
else:
  print("Either")