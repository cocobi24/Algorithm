# https://www.acmicpc.net/problem/1308

import datetime
from_date = datetime.date(*list(map(int,input().split())))
to_date = datetime.date(*list(map(int,input().split())))
d_day = to_date - from_date

if(d_day.days >= 365243) :
    print("gg")
else :
    print(f"D-{d_day.days}", end='')