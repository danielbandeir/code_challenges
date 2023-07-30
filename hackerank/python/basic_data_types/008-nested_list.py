students = []
secondLowest = []
lowest = []

for idxItem in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

students = sorted(students, key=lambda x: x[1]);

lowest.append(students[0])

for idx, currentStudent in enumerate(students):
    if(len(secondLowest) != 0 and currentStudent[1] != secondLowest[0][1]):
        break
    else:
        if(currentStudent[1] > lowest[0][1]):
            secondLowest.append(currentStudent)
        
secondLowest = sorted(secondLowest, key=lambda x: x[0])

for student in secondLowest:
    print(student[0])