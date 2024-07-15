# https://www.acmicpc.net/problem/2864

a, b = list(input().split())

minA = a.replace('6', '5')
maxA = a.replace('5', '6')
minB = b.replace('6', '5')
maxB = b.replace('5', '6')

min = int(minA) + int(minB)
max = int(maxA) + int(maxB)
print(min, max)