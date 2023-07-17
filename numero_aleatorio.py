# import random
# print(random.getrandbits(32))

# from random import choices

# print(*choices([*range(1, 9)], k=10), sep = '')


import random

print(random.getrandbits(1))
#resultado: 0

print(random.getrandbits(2))
#resultado: 2

print(random.getrandbits(8))
#resultado: 30

print(random.getrandbits(16))
#resultado: 56789

print(random.getrandbits(20))
#resultado: 337675

print(random.getrandbits(32))
#resultado: 972043261
