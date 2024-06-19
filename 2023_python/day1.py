def SumOfFirstAndLastDigitsInAString(string):
    sum = 0
    digits = []
    for i,x in enumerate(string):
        if x.isdigit():
            digits.append(x)
        for d,val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if string[i:].startswith(val):
                digits.append(str(d+1))

    sum += int(digits[0]+digits[-1])
    return sum


file = open("input1.txt", "rt")

sum = 0
for line in file:
    sum += SumOfFirstAndLastDigitsInAString(line)


print(sum)
