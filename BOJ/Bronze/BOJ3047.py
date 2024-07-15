# https://www.acmicpc.net/problem/3047

a,b,c = sorted(map(int, input().split()))
s = list(input().rstrip())
ans = {'A':a, 'B':b, 'C':c}
print(ans[s[0]], ans[s[1]], ans[s[2]])