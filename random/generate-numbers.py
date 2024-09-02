from random import choices
from string import digits

print(*[''.join(choices(digits, k=12)) for _ in range(5)], sep = '\n')