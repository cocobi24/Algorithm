# https://www.acmicpc.net/problem/1789

s, i = int(input()), 1
sum = 0
while True :
    if sum > s :
        break
    sum += i
    i += 1

print(i-2, end='')