# https://www.acmicpc.net/problem/1431

import sys
input = sys.stdin.readline
n = int(input())
serial_list = [input().rstrip() for _ in range(n)]

def calculate_sum(serial) :
    sum_value = 0
    for s in serial :
        if s.isdigit() :
            sum_value += int(s)
    return sum_value

serial_list.sort(key=lambda x : (len(x), calculate_sum(x), x))
print(*serial_list, sep="\n")