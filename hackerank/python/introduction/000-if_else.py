def isEven(number):
    return True if number%2 == 0 else False

def textOutput(number):
    if(isEven(number)):
        if(number >=2 and number <=5 or number > 20):
            return 'Not Weird'
        else:
            return 'Weird'
    else:
        return 'Weird'

n = int(input().strip())

print(textOutput(n))

    