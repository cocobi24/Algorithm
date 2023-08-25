# https://www.acmicpc.net/problem/2578

board = [0]
for _ in range(5):
    board += list(map(int, input().split()))

bingo = []
for _ in range(5):
    bingo += list(map(int, input().split()))

for i in range(25):
    idx = board.index(bingo[i])
    board[idx] = -1
    count = 0

    for j in range(1, 26, 5):
        if sum(board[j:j+5]) == -5:
            count += 1

    for j in range(1, 6):
        if board[j] + board[j+5] + board[j+10] + board[j+15] + board[j+20] == -5:
            count += 1

    if sum([board[1], board[7], board[13], board[19], board[25]]) == -5:
        count += 1

    if sum([board[5], board[9], board[13], board[17], board[21]]) == -5:
        count += 1

    if count >= 3 :
        break
    
print(i+1)