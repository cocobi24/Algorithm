# https://www.acmicpc.net/problem/21300

bottle = list(map(int, input().split()))
bottle = [b * 5 for b in bottle]
print(sum(bottle))