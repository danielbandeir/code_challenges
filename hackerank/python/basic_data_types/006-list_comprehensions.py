x = int(input())
y = int(input())
z = int(input())
n = int(input())

def shouldAdd(x, y, z, n):
    return True if ((x+y+z)!=n) else False

returnedList = []

for indX in range(x+1):
    for indY in range(y+1):
        for indZ in range(z+1):
            if(shouldAdd(indX, indY, indZ, n)):
                returnedList.append([indX, indY, indZ])

print(returnedList)