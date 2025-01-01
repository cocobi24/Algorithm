# https://www.acmicpc.net/problem/17293

n = int(input())

def getBottle(i):
  if i == 0:
    return 'no more bottles'
  if i == 1:
    return '1 bottle'
  return f'{i} bottles'

for i in range(n, 0, -1):
  print(f"{getBottle(i)} of beer on the wall, {getBottle(i)} of beer.")
  print(f"Take one down and pass it around, {getBottle(i-1)} of beer on the wall.\n")
print(f"No more bottles of beer on the wall, no more bottles of beer.")
print(f"Go to the store and buy some more, {getBottle(n)} of beer on the wall.")