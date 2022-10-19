# https://www.acmicpc.net/problem/1076

options = {
    'black' : [0, 1]
    , 'brown' : [1, 10]
    , 'red'   : [2, 100]
    , 'orange': [3, 1000]
    , 'yellow': [4, 10000]
    , 'green' : [5, 100000]
    , 'blue'  : [6, 1000000]
    , 'violet': [7, 10000000]
    , 'grey'  : [8, 100000000]
    , 'white' : [9, 1000000000]
}

first = input()
mid = input()
last = input()

resistance  = int(str(options[first][0]) + str(options[mid][0]))
multiValue = options[last][1]
answer = resistance * multiValue
print(answer)