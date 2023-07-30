manipulatedList = []

numRecords = int(input())

for item in range(numRecords):
    itens = input().split()
    if(itens[0] == 'insert'):
        manipulatedList.insert(int(itens[1]), int(itens[2]))
    elif(itens[0] == 'print'):
        print(manipulatedList)
    elif(itens[0] == 'remove'):
        manipulatedList.remove(int(itens[1]))
    elif(itens[0] == 'append'):
        manipulatedList.append(int(itens[1]))
    elif(itens[0] == 'sort'):
        manipulatedList.sort()
    elif(itens[0] == 'pop'):
        manipulatedList.pop(len(manipulatedList)-1)
    elif(itens[0] == 'reverse'):
        manipulatedList.reverse()