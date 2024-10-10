from .State import State
from .FarmerGame import FarmerGame
from typing import Set


def gameReader(filePath: str) -> FarmerGame:
    boolMapping = lambda x: x == "1"

    with open(filePath, "r") as file:
        lines = file.readlines()
        itemNames: tuple[str, ...] = tuple(lines[0].split())
        game = FarmerGame(itemNames)
        State.addItemNames(itemNames)
        source: State = State(list(map(boolMapping, lines[1].split())))
        target: State = State(list(map(boolMapping, lines[2].split())))
        game.setSource(source)
        game.setTarget(target)
        file.close()
    return game


def badStateReader(filePath: str) -> Set[State]:
    boolMapping = lambda x: x == "1"
    with open(filePath, "r") as file:
        lines = file.readlines()
        nBadStates: int = int(lines[0])
        badStates: set[State] = set()
        for i in range(nBadStates):
            state = State(list(map(boolMapping, lines[i + 1].split())))
            badStates.add(state)
        file.close()
    return badStates
