# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    # write your code in Python 2.7
    digits = ""
    count = 0
    for char in S:
        if char.isdigit():
            count += 1
            digits += char

    output = ""
    num_group = int(len(digits)/3)
    for i in range(num_group):
        start_index = i*3
        print(digits[start_index: start_index+3])

    print(output)

    return output

print(solution('00-44  48 5555 8361'))


print
output
output = output[0:-1]