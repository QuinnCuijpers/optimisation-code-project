from .state import State
from .farmerGame import FarmerGame
from typing import Set, List


def gameReader(filePath: str) -> FarmerGame:
    """
    Creates a `FarmerGame` object from a data file.

    The data file should contain the following space-separated information:
    1. A list of item names.
    2. A binary representation of the source state, where `1` at position `i` indicates that item `i` is on the left side.
    3. A binary representation of the target state, where `1` at position `i` indicates that item `i` is on the left side.

    This method reads the item names, the source state, and the target state from the file. It does not initialize the `badStates`
    property; that is done separately via the `badStateReader`.

    ### Example of a valid data file:
        Farmer Wolf Goat Cabbage
        0 0 0 0
        1 1 1 1

    Args:
        filePath (str): Path to the file containing the data for the `FarmerGame` object.

    Returns:
        FarmerGame: The `FarmerGame` object accosiated with the given input file
    """
    boolMapping = lambda x: x == "1"

    with open(filePath, "r") as file:
        lines: List[str] = file.readlines()
        itemNames: tuple[str, ...] = tuple(lines[0].split())
        game = FarmerGame(itemNames)
        State.addItemNames(itemNames)

        source: State = State(list(map(boolMapping, lines[1].split())))
        target: State = State(list(map(boolMapping, lines[2].split())))

        game.setSource(source)
        game.setTarget(target)

    return game


def badStateReader(filePath: str) -> Set[State]:
    """
    Creates a set of states from a file

    the file should contain the following space seperated info:
    1. A number `n` saying how many badSates will be listed below
    2. The next `n` lines represent the binary configurations of the bad states, where `1` at position `i`
    indicates that item `i` is on the left side, and `0` indicates that the item is on the right side.
    ### Example for the Farmer Wolf Goat Cabbage problem :
        6
        0 1 1 0
        0 1 1 1
        0 0 1 1
        1 0 0 1
        1 0 0 0
        1 1 0 0


    Args:
        filePath (str): path to the file containing the data for the badStates.

    Returns:
        Set[State]: A set of `State` objects representing the bad states.
    """
    boolMapping = lambda x: x == "1"
    with open(filePath, "r") as file:
        lines = file.readlines()
        nBadStates: int = int(lines[0])
        badStates: set[State] = set()
        for i in range(nBadStates):
            state = State(list(map(boolMapping, lines[i + 1].split())))
            badStates.add(state)
    return badStates
