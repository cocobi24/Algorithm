# https://www.acmicpc.net/problem/10768

month = input()
day = input()
day = '0'+day if len(day) == 1 else day
ans = int(month+day)
if ans < 218:
    print("Before")
elif ans == 218:
    print("Special")
else:
    print("After")