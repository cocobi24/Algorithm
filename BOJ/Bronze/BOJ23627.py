# https://www.acmicpc.net/problem/23627

s = input().rstrip()
ans = "cute" if s[len(s)-5:] == "driip" else "not cute"
print(ans)