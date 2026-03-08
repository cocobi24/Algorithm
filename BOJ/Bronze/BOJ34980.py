# https://www.acmicpc.net/problem/34980

n = int(input())
before = list(input().rstrip())
after = list(input().rstrip())

b_cnt = 0
a_cnt = 0
diff = 0
for i in range(n):
     if before[i] != after[i]:
          diff += 1
     if before[i] == 'w':
          b_cnt += 1
     if after[i] == 'w':
          a_cnt += 1

if a_cnt > b_cnt:
     print("Manners maketh man")
elif b_cnt > a_cnt:
     print("Oryang")
elif b_cnt == a_cnt and diff > 0:
     print("Its fine")
else:
     print("Good")