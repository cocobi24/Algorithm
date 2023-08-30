# https://www.acmicpc.net/problem/14003

from bisect import bisect_left
n, nums = int(input()), list(map(int, input().split()))

lis, bis = [], []
for num in nums:
    if not lis or lis[-1] < num:
        lis.append(num)
        bis.append((len(lis)-1, num))
    else:
        lis[bisect_left(lis, num)] = num
        bis.append((bisect_left(lis, num), num))
print(len(lis))

ans, start, end = [], len(bis)-1, len(lis)-1
for i in range(start, -1, -1):
    if bis[i][0] == end:
        ans.append(bis[i][1])
        end -= 1
print(*ans[::-1])