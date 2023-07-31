word = input()

alnum = alpha = digit = lower = upper = False

for letter in word:
    if(letter.isalnum()): alnum = True 
    if(letter.isalpha()): alpha = True 
    if(letter.isdigit()): digit = True 
    if(letter.islower()): lower = True 
    if(letter.isupper()): upper = True 

print(alnum)
print(alpha)
print(digit)
print(lower)
print(upper)