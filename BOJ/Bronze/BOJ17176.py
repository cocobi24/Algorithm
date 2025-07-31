# https://www.acmicpc.net/problem/32929

dic = { 0: ' ' }
for i in range(1, 27):
    dic[i] = chr(i+64)
for i in range(27, 53):
    dic[i] = chr(i+70)

n = int(input())
dec = [dic[int(i)] for i in input().rstrip().split()]
dec.sort()
s = sorted(input().rstrip())
print('y' if dec == s else 'n')