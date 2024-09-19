# https://www.acmicpc.net/problem/6032

N = int(input())
toy_list = []
for i in range(1, N+1):
  joy, price = map(int, input().split())
  happy = joy / price
  toy_list.append([i, happy, price])
toy_list.sort(key=lambda x: -x[1])
pay = sum([toy_list[i][2] for i in range(3)])
print(pay)
print(*[toy_list[i][0] for i in range(3)], sep='\n')