# https://www.acmicpc.net/problem/15953

import sys
input = sys.stdin.readline
T = int(input())
prize_2017 = { 1: 5000000, 2: 3000000, 3: 2000000, 4: 500000, 5: 300000, 6: 100000 }
prize_2018 = { 1: 5120000, 2: 2560000, 3: 1280000, 4: 640000, 5: 320000 }

def getPrize2017(n):
  if    n == 1:       return prize_2017[1]
  elif  1 < n <= 3:   return prize_2017[2]
  elif  3 < n <= 6:   return prize_2017[3]
  elif  6 < n <= 10:  return prize_2017[4]
  elif  10 < n <= 15: return prize_2017[5]
  elif  15 < n <= 21: return prize_2017[6]
  return 0
def getPrize2018(n):
  if    n == 1:       return prize_2018[1]
  elif  1 < n <= 3:   return prize_2018[2]
  elif  3 < n <= 7:   return prize_2018[3]
  elif  7 < n <= 15:  return prize_2018[4]
  elif  15 < n <= 31: return prize_2018[5]
  return 0

for _ in range(T):
  a, b = map(int, input().split())
  answer = getPrize2017(a) + getPrize2018(b)
  print(answer)