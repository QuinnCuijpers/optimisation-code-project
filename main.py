from src.farmerGame.farmerGame import FarmerGame
from src.farmerGame.state import State
from typing import Set
from src.farmerGame.dataReader import game_reader, bad_state_reader


if __name__ == "__main__":

    game: FarmerGame = game_reader(
        "./data/Data.txt")  # change to ./data/alphabetData.txt for example 2 or ./data/piratesData.txt for example 3
    badStates: Set[State] = bad_state_reader(
        "./data/BadStates.txt"
    )  # change to ./data/alphabetBadStates.txt for example 2 or ./data/piratesBadStates.txt for example 3
    game.add_bad_states(badStates)

    print(f"starting state of the game: {game.source}")
    print(f"ending state of the game: {game.target}")

    path, result = game.bfs(print_actions=True)
    if result:
        print(
            f"path from start to end found with {len(path) - 1} steps: {list(map(str, path))}"
        )
    else:
        print(f"No path from {game.source} to {game.target} found")
