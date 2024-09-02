import time
from itertools import cycle

cores = {
			'clear':'\033[m',
			'red':'\033[31m',
			'green':'\033[32m',
			'yellow':'\033[33m',
			'azulescuro':'\033[34m',	
			'roxo':'\033[35m',
			'azulclaro':'\033[36m',	
			'pretoebranco':'\033[7;30m',	
        }

lights = [('Green', 2),('Yellow', 0.5),('Red', 2)]

colors = cycle(lights)

while True:
    c,s = next(colors)
    print(c)
    time.sleep(s)