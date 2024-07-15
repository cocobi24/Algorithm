# https://www.acmicpc.net/problem/27964

n = int(input())
topping_set = set(map(str, input().rstrip().split()))
topping_list = list(topping_set)
cheese_list = list(filter(lambda x: x[-6::] == "Cheese", topping_list))
print("yummy" if len(cheese_list) >= 4 else "sad")