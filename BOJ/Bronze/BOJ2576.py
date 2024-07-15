# https://www.acmicpc.net/problem/2576

min_value = 101
sum_value = 0

for _ in range(7) :
    n = int(input())
    if n % 2 != 0 :
        sum_value += n
        if min_value > n :
            min_value = n
if sum_value == 0 :
    print(-1)
else :
    print(sum_value, min_value, sep="\n")