# Módulo de tempo Python

# https://www.programiz.com/python-programming/time

from datetime import datetime
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
# data brasil
print('%s/%s/%s' % (now.day, now.month, now.year))
# hora brasil
print('%s:%s:%s' % (now.hour, now.minute, now.second))

print('%s/%s/%s - %s:%s:%s' % (now.day, now.month, now.year, now.hour, now.minute, now.second))

data = ('%s/%s/%s - %s:%s:%s' % (now.day, now.month, now.year, now.hour, now.minute, now.second))
print(data,".txt")