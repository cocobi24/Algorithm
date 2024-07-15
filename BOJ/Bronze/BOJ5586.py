# https://www.acmicpc.net/problem/5586

S = input().rstrip()
JOI, IOI = 0, 0
for i in range(len(S)-2):
  if S[i:i+3] == "JOI":
    JOI += 1
  elif S[i:i+3] == "IOI":
    IOI += 1
print(JOI, IOI, sep='\n')