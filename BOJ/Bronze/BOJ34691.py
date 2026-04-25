# https://www.acmicpc.net/problem/34691

import sys
input = sys.stdin.readline

dic = {
    'animal': 'Panthera tigris',
    'tree': 'Pinus densiflora',
    'flower': 'Forsythia koreana'
}

while True:
    key = input().rstrip()
    if key == 'end':
        exit()
    print(dic[key])