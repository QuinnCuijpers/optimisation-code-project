from .state import State
from .farmerGame import FarmerGame
from typing import Set, List


def game_reader(file_path: str) -> FarmerGame:
    """
    Creates a `FarmerGame` object from a data file.

    The data file should contain the following space-separated information:
    1. A list of item names.
    2. A binary representation of the source state, where `1` at position `i` indicates that item `i` is on the left side.
    3. A binary representation of the target state, where `1` at position `i` indicates that item `i` is on the left side.

    This method reads the item names, the source state, and the target state from the file. It does not initialize the `bad_states`
    property; that is done separately via the `badStateReader`.

    ### Example of a valid data file:
        Farmer Wolf Goat Cabbage
        0 0 0 0
        1 1 1 1

    Args:
        file_path (str): Path to the file containing the data for the `FarmerGame` object.

    Returns:
        FarmerGame: The `FarmerGame` object associated with the given input file
    """
    def bool_mapping(x): return x == "1"

    with open(file_path, "r") as file:
        lines: List[str] = file.readlines()
        item_names: tuple[str, ...] = tuple(lines[0].split())
        game = FarmerGame(item_names)
        State.add_item_names(item_names)

        source: State = State(list(map(bool_mapping, lines[1].split())))
        target: State = State(list(map(bool_mapping, lines[2].split())))

        game.set_source(source)
        game.set_target(target)

    return game


def bad_state_reader(file_path: str) -> Set[State]:
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
        file_path (str): path to the file containing the data for the bad_states.

    Returns:
        Set[State]: A set of `State` objects representing the bad states.
    """
    def bool_mapping(x): return x == "1"

    with open(file_path, "r") as file:
        lines: List[str] = file.readlines()
        n_bad_states: int = int(lines[0])
        bad_states: set[State] = set()
        for i in range(n_bad_states):
            state = State(list(map(bool_mapping, lines[i + 1].split())))
            bad_states.add(state)
    return bad_states
