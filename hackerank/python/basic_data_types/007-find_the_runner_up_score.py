n = int(input())
arr = map(int, input().split())

highScore = -100
runnerUpScore = -100

for score in sorted(list(arr)):
    if score > highScore:
        runnerUpScore = highScore
        highScore = score

print(runnerUpScore)