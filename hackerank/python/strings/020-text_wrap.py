def wrap(string, max_width):
    wrappedText = ''
    for idxLetter in range(0, len(string), max_width):
        wrappedText+=(string[idxLetter:idxLetter+max_width]+'\n')
    return wrappedText
        

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)