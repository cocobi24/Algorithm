# https://www.acmicpc.net/problem/2331

A, P = map(int, input().split())
D = [A]

while True:
    sum_value = 0
    for i in (str(D[-1])):
        sum_value += int(i) ** P
    if sum_value in D:
        while True:
            if sum_value == D.pop():
                print(len(D))
                exit()
    else:
        D.append(sum_value)