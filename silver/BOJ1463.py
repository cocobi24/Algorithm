# https://www.acmicpc.net/problem/1463

n = int(input())
temp = [0] * (n+1)

for i in range(2, n+1) :
    temp[i] = temp[i-1] + 1
    if i % 2 == 0 :
        temp[i] = min(temp[i], temp[i//2]+1)
    if i % 3 ==0 :
        temp[i] = min(temp[i], temp[i//3] + 1)

print(temp[n])
