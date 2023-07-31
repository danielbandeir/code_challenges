def swap_case(word):
    convertedWord = '';
    for letter in word:
        if letter.islower():
            convertedWord+=letter.upper()
        else:
            convertedWord+=letter.lower()
    return convertedWord


s = input()
print(swap_case(s))