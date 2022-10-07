# https://www.acmicpc.net/problem/10828

import sys
input = sys.stdin.readline
n =  int(input())

class Stack :
    stack = []
    def command(self, command, x=None):
        if command == "push" :
            self.stack.insert(0, x)

        elif command == "pop" :
            if len(self.stack) == 0 :
                return print(-1)
            num = self.stack.pop(0)
            print(num)

        elif command == "size" :
            print(len(self.stack))

        elif command == "empty" :
            if len(self.stack) == 0:
                print(1)
            else :
                print(0)

        elif command == "top" :
            if len(self.stack) == 0:
                return print(-1)
            num = self.stack.pop(0)
            self.stack.insert(0, num)
            print(num)

myStack = Stack()
for i in range(n) :
    commands = input().split()
    if len(commands) == 1 :
        myStack.command(commands[0])
    else :
        myStack.command(commands[0], commands[1])