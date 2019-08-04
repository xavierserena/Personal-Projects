lineLength = 29
print(" "*5 + "*"*6 + " "*7 + "*"*6)
print(" "*3 + "*"*10 + " "*3 + "*"*10)
for _ in range(int(lineLength/9)):
    print("*"*lineLength)
for i in range(1, int(lineLength/2), 2):
    a = lineLength - 2*i
    print(" "*i + "*"*a + " "*i)
s = int(lineLength/2)
print(" "*s + "*" + " "*s)