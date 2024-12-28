# https://www.acmicpc.net/problem/25183

N = int(input())
s = input().strip()
answer = "NO"
for i in range(N - 4):
  substring = s[i:i + 5]
  check_list = [abs(ord(substring[j]) - ord(substring[j + 1])) == 1 for j in range(4)]
  if all(check_list):
    answer = "YES"
    break
  answer = "NO"
print(answer)