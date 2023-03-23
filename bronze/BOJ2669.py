# https://www.acmicpc.net/problem/2669

coordinate = []

for i in range(4) :
    x1, y1, x2, y2 = map(int, input().split())
    x = x1
    y = y1
    while x != x2 :
        y = y1
        x += 1
        while y != y2 :
            y += 1
            coordinate.append((x,y))
    if x1 == x2 and y1 == y2 :
        coordinate.append((x, y))

print(len(set(coordinate)))