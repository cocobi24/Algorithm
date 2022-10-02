# https://www.acmicpc.net/problem/18870

n = int(input())
nums = list(map(int, input().split()))
uniqueArr = sorted(list(set(nums)))
dic = {}

for i in range(len(uniqueArr)) :
    dic[uniqueArr[i]] = i

for i in nums:
    print(dic[i], end = ' ')