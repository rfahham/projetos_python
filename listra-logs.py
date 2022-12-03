from datetime import datetime,timedelta

now = datetime.now()

s = [(now - timedelta(minutes=x)).strftime("%b%e %H:%M")
    for x in range(10)]

with open('/var/log/syslog') as opf:
    rd = opf.readlines()

for i in rd:
    j = ' '.join(i.split()[:3])
    if j.rpartition(':')[0] in s:
        print(i.strip)