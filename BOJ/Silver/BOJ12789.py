# https://www.acmicpc.net/problem/12789

n = int(input())
student = list(map(int, input().split()))
sorted_student = sorted(student)

main, sub = [], []
for s in student:
  if s == len(main)+1:
    main.append(s)
    while True:
      if len(sub) == 0:
        break

      if sub[-1] == len(main)+1:
        main.append(sub.pop())
      else:
        break
  else:
    sub.append(s)

print("Nice" if main == sorted_student else "Sad")