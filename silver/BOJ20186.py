# https://www.acmicpc.net/problem/20186

N, K = map(int, input().split())
nums = sorted(map(int, input().split()), reverse=True)
ans = sum(nums[:K]) - sum(range(K))
print(ans)