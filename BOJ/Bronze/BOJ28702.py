# https://www.acmicpc.net/problem/28702

a = input().rstrip()
b = input().rstrip()
c = input().rstrip()
quest = [a, b, c]
quest_bool = [a.isnumeric(), b.isnumeric(), c.isnumeric()]
idx = quest_bool.index(True)
target = int(quest[idx]) + 3 - idx

if target % 3 == 0 and target % 5 == 0:
  print("FizzBuzz")
elif target % 3 == 0:
  print("Fizz")
elif target % 5 == 0:
  print("Buzz")
else:
  print(target)