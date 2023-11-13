# https://www.acmicpc.net/problem/14584

import sys
input = sys.stdin.readline

def solv(pwd, n, words):
  for i in range(26):
    decryption = ""
    for pw in pwd:
      decryption += chr(((ord(pw) - 97 + i) % 26) + 97)

    for j in range(n):
      if words[j] in decryption:
        return decryption

pwd, n = input()[:-1], int(input())
words = [input().rstrip() for _ in range(n)]
print(solv(pwd, n, words))