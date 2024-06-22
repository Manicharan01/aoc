import re
visited = list()


def CharacterLocater(pattern):
    # This function takes a pattern as input and returns the location of Special characters and numbers in the pattern
    # The pattern is a string of characters
    characters = ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@']
    numbers = '^[0-9]+$'
    dirs = [
            [-1, 1], [0, 1], [1, 1],
            [-1, 0], [1, 0],
            [-1, -1], [0, -1], [1, -1]
    ]
    numbers_encountered = []
    special_characters_encountered = []
    i = 0
    j = 0
    total_sum = 0
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            for character in characters:
                if character in pattern[i][j]:
                    special_characters_encountered.append((i, j))
            if re.match(numbers, pattern[i][j]):
                numbers_encountered.append((i, j))

    for a, b in special_characters_encountered:
        for x, y in dirs:
            if 0 <= a + x < len(pattern) and 0 <= b + y < len(pattern[0]):
                if (a + x, b + y) in numbers_encountered and (a + x, b + y) not in visited:
                    total_sum += NumberFinder(pattern, a + x, b + y)

    print(total_sum)


def NumberFinder(line, x, y):
    i = y
    sum = ''
    while line[x][i] != '.':
        if line[x][i].isdigit():
            sum = line[x][i] + sum
            visited.append((x, i))
        i = i - 1
    j = y + 1
    while line[x][j] != '.' and j < len(line[x]):
        if line[x][j].isdigit():
            sum += line[x][j]
            visited.append((x, j))
        j = j + 1
        if j == len(line[x]):
            break
    sum = int(sum)
    return sum


file = open('input3.txt', 'r')
pattern = file.readlines()
CharacterLocater(pattern)
