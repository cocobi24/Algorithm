# https://www.acmicpc.net/problem/5349

numbers = set()
overlap = set()
while True:
  number = input().rstrip()
  if number == '000-00-0000':
    break
  if number not in numbers:
    numbers.add(number)
  else:
    overlap.add(number)
print(*sorted(overlap), sep='\n')