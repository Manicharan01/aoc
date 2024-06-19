import typing as t
from dataclasses import dataclass


@dataclass
class Round:
    red: int = 0
    green: int = 0
    blue: int = 0

    @classmethod
    def from_input(cls, text: str) -> t.Self:
        parts = [pair.strip().partition(" ") for pair in text.split(",")]
        return cls(**{name.strip(): int(value) for value, _, name in parts})


@dataclass
class Game:
    id: int
    rounds: t.Sequence[Round]

    @classmethod
    def from_line(cls, line: str) -> t.Self:
        identifier, _, remainder = line.partition(":")
        number = int(identifier.partition(" ")[-1])
        rounds = [Round.from_input(part.strip()) for part in remainder.split(";")]
        return cls(number, tuple(rounds))

    def is_possible(self, red: int, green: int, blue: int) -> bool:
        return all(
            round.red <= red and round.green <= green and round.blue <= blue
            for round in self.rounds
        )


file = open("input2.txt", "rt")
test_games = [Game.from_line(line) for line in file.readlines()]
print(test_games)
print(sum(game.id for game in test_games if game.is_possible(12, 13, 14)))
