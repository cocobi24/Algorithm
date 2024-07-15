# https://www.acmicpc.net/problem/11582

N = int(input())
store = list(map(int, input().split()))
K =  int(input())

idx = N // K
sortedList = []
for i in range(0, N, idx):
  sortedList += sorted(store[i:i+idx])

print(*sortedList)