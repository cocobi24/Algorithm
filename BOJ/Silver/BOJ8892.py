# https://www.acmicpc.net/problem/8892

import sys
input = sys.stdin.readline
n = int(input())
answer = [0] * n

for i in range(n) :
  K = int(input())
  word_list = [input().rstrip() for _ in range(K)]
  isPalindrome = False

  for j in range(K) :
    for k in range(K):
      if j != k :
        word = word_list[j] + word_list[k]

        for idx in range(len(word)//2) :
          if word[idx] != word[-idx-1] :
            isPalindrome = False
            break
          isPalindrome = True

      if isPalindrome :
        answer[i] = word
        break
    if isPalindrome:
      break

  print(answer[i])