from __future__ import print_function
import numpy as np
import datetime
import re

dts = []
acts = {}
with open('./input.txt') as f_input:
    for line in f_input:
        dt, act = [x.strip() for x in re.split(r'[\[\]]', line.strip())[1:]]
        dts.append(dt)
        acts[dt] = act
dts.sort()
acts = sorted(acts.items())

i = 0
guards = {}
schedule = {}
for date_time, action in acts:
    date, time = date_time.split(' ')
    if time[0] != '0':
        year, month, day = [int(x) for x in date.split('-')]
        date = datetime.date(year, month, day) + datetime.timedelta(days=1)
        year = str(date.year)
        month = str(date.month)
        if len(month) == 1:
            month = '0' + month
        day = str(date.day)
        if len(day) == 1:
            day = '0' + day
        date = year + '-' + month + '-' + day
    if time[0] == '0':
        time = str(int(time[:1]) + 24) + time[2:]
    if date in schedule:
        schedule[date][time] = action
    else:
        schedule[date] = {time : action}
        g = action.split(' ')[1].strip('#')
        if g not in guards:
            guards[g] = i
            i += 1
guards_inv = {v:k for k, v in guards.iteritems()}

for date in schedule:
    schedule[date] = sorted(schedule[date].items())

schedule = sorted(schedule.items())
records = np.zeros([i, 60])
for date, x in schedule:
    g = x[0][1].split(' ')[1].strip('#')
    for act in x[1:]:
        time, action = act
        for i in range(int(time[-2:]), 60):
            if action[0] == 'f':
                records[guards[g]][i] += 1
            else:
                records[guards[g]][i] -= 1

#SOLUTION TO PART 1
sleep = records.sum(axis=1)
sleep_guard = np.argmax(sleep)
sleep_minute = np.argmax(records[sleep_guard])
print(int(guards_inv[sleep_guard])*sleep_minute)

#SOLUTION TO PART 2
coords = np.unravel_index(records.argmax(), records.shape)
print(int(guards_inv[coords[0]])*coords[1])
