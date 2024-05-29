# https://www.acmicpc.net/problem/6736

limit = int(input().rstrip())
speed = int(input().rstrip())
over = speed - limit

if speed > limit:
  if 1 <= over <= 20:
    print("You are speeding and your fine is $100.")
  elif 21 <= over <= 30:
    print("You are speeding and your fine is $270.")
  else:
    print("You are speeding and your fine is $500.")
else:
  print("Congratulations, you are within the speed limit!")