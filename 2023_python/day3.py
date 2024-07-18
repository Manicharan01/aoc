def CharacterLocater(pattern):
    # This function takes a pattern as input and returns the location of Special characters and numbers in the pattern
    # The pattern is a string of characters
    visited = set()
    i = 0
    for i in range(len(pattern)):
        j = 0
        for j in range(len(pattern[i])):
            if pattern[i][j].isdigit() or pattern[i][j] == ".":
                continue
            for current_row in [i - 1, i, i + 1]:
                for current_coloumn in [j - 1, j, j + 1]:
                    if (
                        current_row < 0
                        or current_row >= len(pattern)
                        or current_coloumn < 0
                        or current_coloumn >= len(pattern[current_row])
                        or not pattern[current_row][current_coloumn].isdigit()
                    ):
                        continue
                    while (
                        current_coloumn > 0
                        and pattern[current_row][current_coloumn - 1].isdigit()
                    ):
                        current_coloumn = current_coloumn - 1
                    visited.add((current_row, current_coloumn))

    summation = []
    for r, c in visited:
        number = ""
        while c < len(pattern[r]) and pattern[r][c].isdigit():
            number += pattern[r][c]
            c = c + 1
        print(number)
        summation.append(int(number))

    print(summation)
    print(sum(summation))


file = open("input3.txt", "r")
pattern = file.readlines()
CharacterLocater(pattern)
