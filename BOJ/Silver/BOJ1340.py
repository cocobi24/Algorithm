# https://www.acmicpc.net/problem/1340

month_list = ["January" , "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month, day, year, time = input().split()
day = int(day[:-1])
year = int(year)
hour, minute = map(int, time.split(':'))
idx = month_list.index(month)

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    day_list[1] += 1

total = sum(day_list) * 24 * 60
current = (sum(day_list[:idx]) + day-1)*24*60 + hour*60 + minute
answer = current/total * 100
print(answer)