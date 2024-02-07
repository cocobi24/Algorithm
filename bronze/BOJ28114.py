# https://www.acmicpc.net/problem/28114

student = list(list(map(str, input().split())) for _ in range(3))

for i in range(3):
  student[i][1] = int(student[i][1]) % 100
  student[i][2] = student[i][2][0]

student.sort(key=lambda x: x[1])
print(str(student[0][1]) + str(student[1][1]) + str(student[2][1]))

student.sort(key=lambda x: -int(x[0]))
print(student[0][2] + student[1][2] + student[2][2])