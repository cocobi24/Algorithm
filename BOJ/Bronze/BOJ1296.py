# https://www.acmicpc.net/problem/1296

import sys
input = sys.stdin.readline
name = input().rstrip()
n = int(input())
name_value = {
    'L': name.count('L'),
    'O': name.count('O'),
    'V': name.count('V'),
    'E': name.count('E')
}

rank_list = []
for _ in range(n) :
    team_name = input().rstrip()
    L = team_name.count('L') + name_value['L']
    O = team_name.count('O') + name_value['O']
    V = team_name.count('V') + name_value['V']
    E = team_name.count('E') + name_value['E']
    value = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    rank_list.append((team_name, value))

rank_list = sorted(rank_list, key=lambda x : (-x[1], x[0]))
print(rank_list[0][0])