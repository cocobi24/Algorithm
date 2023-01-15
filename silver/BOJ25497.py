# https://www.acmicpc.net/problem/25497

n = int(input())
input_list = list(input())
count = 0
l_cnt = 0
s_cnt = 0

for i in input_list :
    if i == 'L' :
        l_cnt += 1
    elif i == "S" :
        s_cnt += 1
    elif i == "R" :
        if l_cnt >= 1 :
            l_cnt -= 1
            count += 1
        else :
            break
    elif i == "K" :
        if s_cnt >= 1 :
            s_cnt -= 1
            count += 1
        else :
            break
    else :
        count += 1

print(count)