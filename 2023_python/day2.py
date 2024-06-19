power = 0


def SumOfGameIDofPossibleGames(line):
    game = line.split(":")
    gameID = game[0].split(" ")
    gameID = int(gameID[1])
    draws = game[1].split(";")

    colors = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for draw in draws:
        DrawSortedbyColor = draw.split(",")
        for color in DrawSortedbyColor:
            specificColor = color.split(" ")
            specificColor[2] = specificColor[2].replace("\n", "")
            colors.update(
                {
                    specificColor[2]: max(
                        colors.get(specificColor[2]), int(specificColor[1])
                    )
                }
            )

    cube = colors.get("red") * colors.get("green") * colors.get("blue")
    return cube

    """
    CubePowerCalculator(colors)
    if (
        colors.get("red") <= 12
        and colors.get("green") <= 13
        and colors.get("blue") <= 14
    ):
        return gameID
    else:
        return 0
    """


# def CubePowerCalculator(colors):
#    global power += colors.get("red") * colors.get("green") * colors.get("blue")


file = open("input2.txt", "rt")

sum = 0

for line in file:
    sum += SumOfGameIDofPossibleGames(line)


print(sum)
# print(power)
