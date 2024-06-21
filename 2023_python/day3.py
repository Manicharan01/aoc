import re


def CharacterLocater(pattern):
    # This function takes a pattern as input and returns the location of Special characters and numbers in the pattern
    # The pattern is a string of characters
    characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '_', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '?', '/', '`', '~']
    numbers = '^[0-9]+$'
    numbers_encountered = []
    special_characters_encountered = []
    i = 0
    j = 0
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            for character in characters:
                if character in pattern[i][j]:
                    special_characters_encountered.append((i, j))
            if re.match(numbers, pattern[i][j]):
                numbers_encountered.append((i, j))

    print(f"Special Characters Encountered at: {special_characters_encountered}")
    print(numbers_encountered)


file = open('input3.txt', 'r')
pattern = file.readlines()
CharacterLocater(pattern)
