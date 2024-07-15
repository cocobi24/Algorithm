# https://www.acmicpc.net/problem/11444

n = int(input())
object = 1000000007
def solv(n):
  if n == 1:
    return [[1, 1],[1, 0]]
  else:
    t = solv(n//2)
    t2 = [[0,0],[0,0]]
    t2[0][0] = (t[0][0]**2 + t[0][1] * t[1][0]) % object
    t2[0][1] = (t[0][0] * t[0][1] + t[0][1] * t[1][1]) % object
    t2[1][0] = (t[1][0] * t[0][0] + t[1][1] * t[1][0]) % object
    t2[1][1] = (t[1][0] * t[0][1] + t[1][1]**2) % object

    if n & 1:
      t[0][0] = (t2[0][0] + t2[1][0]) % object
      t[0][1] = (t2[0][1] + t2[1][1]) % object
      t[1][0] = t2[0][0]
      t[1][1] = t2[0][1]
      return t
    return t2

answer = solv(n)[0][1]
print(answer)