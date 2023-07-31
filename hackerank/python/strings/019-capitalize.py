
# Complete the solve function below.
def solve(s):
    capitalizedName = ''
    for name in s.split(" "):
        capitalizedName+=(name.capitalize()+" ")
    return capitalizedName

s = input()

print(solve(s))