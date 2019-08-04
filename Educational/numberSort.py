digits = '1234567890'

def getInput():
    # number = input('Input a number: ')

    for n in number:
        if n not in digits:
            print('Input is not a number')
            number = input('Input a number')

print(number)
