# https://www.acmicpc.net/problem/14912

n, d = map(int, input().split())
nums = [str(i) for i in range(1,n+1)]
answer = 0

for num in nums :
    answer += num.count(str(d))
print(answer)