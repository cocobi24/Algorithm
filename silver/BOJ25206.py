# https://www.acmicpc.net/problem/25206

import sys
input = sys.stdin.readline
trans_point = {
    "A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0,
    "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0,
    "F" : 0
}

total, res = 0, 0
while True :
    obj_info = list(input().split())
    if len(obj_info) == 0 :
        break
    credit = float(obj_info[1])
    grade = obj_info[2]
    if grade != "P" :
        total += credit
        res += credit * trans_point[grade]

print('%.6f' % (res / total))