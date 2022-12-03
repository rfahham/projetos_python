# pip install matplotlib

import matplotlib.pyplot as p

s = [40, 30, 10, 10, 10]

l = ["Python", "Java", "C++", "C", "JavaScript"]

p.pie(s, labels = l)
p.show()