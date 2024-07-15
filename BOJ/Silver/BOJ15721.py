# https://www.acmicpc.net/problem/15721

a, t = int(input()), int(input())
signal = int(input())

def find_man(sign, target):
    global man
    if signal == sign and target == t:
        print(man)
        exit(0)
    man += 1
    if man >= a:
        man = 0

man, fun, daegi, i = 0, 0, 0, 2
while True:
    for _ in range(2):
        fun += 1
        find_man(0, fun)
        daegi += 1
        find_man(1, daegi)

    for _ in range(i):
        fun += 1
        find_man(0, fun)

    for _ in range(i):
        daegi += 1
        find_man(1, daegi)
    i += 1
