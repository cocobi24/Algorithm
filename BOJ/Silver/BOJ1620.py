# https://www.acmicpc.net/problem/1620

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
name_dic = {}
number_dic = {}
for i in range(1, n+1) :
    temp = input().rstrip()
    name_dic[temp] = i
    number_dic[i] = temp

for i in range(m) :
    target = input().rstrip()

    if target in name_dic :
        print(name_dic[target])
    elif int(target) in number_dic :
            print(number_dic[int(target)])
