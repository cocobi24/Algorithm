# https://www.acmicpc.net/problem/10798

str_list = [input() for _ in range(5)]
length_list = [len(str_list[i]) for i in range(5)]
l = max(length_list)

for i in range(l) :
    for j in range(5) :
        if len(str_list[j]) <= i:
            continue
        print(str_list[j][i], end='')
