# https://www.acmicpc.net/problem/14582

uj = list(map(int, input().split()))
sg = list(map(int, input().split()))
a = 0
b = 0
flag = 0

for i in range(9) :
    a += uj[i]
    if a > b :
        flag = 1
        break
    b += sg[i]

if flag == 1 and (sum(uj) < sum(sg)) :
    print("Yes")
else :
    print("No")