values = [20, 42, 48, 61, 64, 70, 79]
sequence = []
hexstr = ""
for i in range(10):
    sequence[i] = f(i)
for i in range(10):
    letter = hexToLetter(sequence[i])
    str += letter + " "
print(str)

