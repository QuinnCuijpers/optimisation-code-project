from src.farmerGame import FarmerGame
from src.state import State
from typing import Set
from src.dataReader import gameReader, badStateReader


if __name__ == "__main__":

    game: FarmerGame = gameReader(
        "./data/data.txt"
    )  # change to ./data/alphabetData.txt for example 2
    badStates: Set[State] = badStateReader(
        "./data/badStates.txt"
    )  # change to ./data/alphabetBadStates.txt for example 2
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
