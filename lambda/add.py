print("Utilizando função")

def add(x, y):
    return x+y
print("O total da soma: ", add(10, 20))

print()

print("Utilizando lambda")

print("O total da soma: ",(lambda x,y: x+y)(10,20))