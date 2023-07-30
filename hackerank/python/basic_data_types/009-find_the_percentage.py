n = int(input())

student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

sumItens = 0

for valueToSum in student_marks[query_name]:
    sumItens += valueToSum

print("{:.2f}".format(sumItens/3))