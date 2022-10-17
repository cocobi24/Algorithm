# https://www.acmicpc.net/problem/1439

s = input()
one = s.replace('1',' ').split(' ')
one = len(list(filter(None, one)))
zero = s.replace('0',' ').split(' ')
zero = len(list(filter(None, zero)))

answer = zero if one > zero else one
print(answer, end='')