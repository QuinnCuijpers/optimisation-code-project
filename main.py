from src.farmerGame import FarmerGame
from src.state import State
from typing import Set
from src.dataReader import gameReader, badStateReader


if __name__ == "__main__":

    game: FarmerGame = gameReader(
        "./data/Data.txt"
    )  # change to ./data/alphabetData.txt for example 2 or ./data/piratesData.txt for example 3
    badStates: Set[State] = badStateReader(
        "./data/BadStates.txt"
    )  # change to ./data/alphabetBadStates.txt for example 2 or ./data/piratesBadStates.txt for example 3
    game.addBadStates(badStates)

    print(f"starting state of the game: {game.source}")
    print(f"ending state of the game: {game.target}")

    path, result = game.bfs(printActions=True)
    if result:
        print(
            f"path from start to end found with {len(path) - 1} steps: {list(map(str, path))}"
        )
    else:
        print(f"No path from {game.source} to {game.target} found")
