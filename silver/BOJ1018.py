# https://www.acmicpc.net/problem/1018

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
chess_board = []
answers = []

for _ in range(n) :
    chess_board.append(input().rstrip())

for i in range(n-7) :
    for j in range(m-7) :
        B = 0
        W = 0

        for x in range(i, i+8) :
            for y in range(j, j+8) :
                if(x+y) % 2 == 0 :
                    if chess_board[x][y] != "B" :
                        B += 1
                    if chess_board[x][y] != "W" :
                        W += 1
                else :
                    if chess_board[x][y] != "W" :
                        B += 1
                    if chess_board[x][y] != "B" :
                        W += 1

        answers.append(min(B, W))

print(min(answers), end='')