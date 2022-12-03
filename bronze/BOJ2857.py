# https://www.acmicpc.net/problem/2857

flag = 0
for i in range(5) :
    if 'FBI' in input() :
        flag = 1
        print(i+1, end=' ')

if flag == 0 :
    print("HE GOT AWAY!", end='')