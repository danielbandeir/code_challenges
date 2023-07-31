def count_substring(string, sub_string):
    count = 0

    for idx, letter in enumerate(string):
        if idx+len(sub_string) > len(string):
            break
        else: 
            if(string[idx:idx+len(sub_string)] == sub_string):
                count+=1

    return count


string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)