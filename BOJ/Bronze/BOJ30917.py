# https://www.acmicpc.net/problem/30917

def getAnswer(s):
  for i in range(1, 10):
    print(f"? {s}", i, flush=True)
    res = int(input())

    if res == 1:
      return i

A = getAnswer("A")
B = getAnswer("B")
print("!", A + B)