# https://www.acmicpc.net/problem/31866

game = [0, 2, 5]
hand = ['J', 'K', 'B']

def getHand(h):
    if h in game:
        return hand[game.index(h)]
    return "ERR"

def getWinner(a, b):
    if ((a == 'J' and b == 'K')
            or (a == 'K' and b == 'B')
            or (a == 'B' and b == 'J')
            or (a != 'ERR' and b == 'ERR')):
        return True
    return False

js, ij = map(int, input().split())
JS, IJ = getHand(js), getHand(ij)

if JS == IJ:
    print('=')
    exit(0)

if getWinner(JS, IJ):
   print('>')

if getWinner(IJ, JS):
    print('<')