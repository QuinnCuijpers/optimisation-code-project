from typing import List, Set, Optional, Deque
from .state import State
from collections import deque
from collections.abc import Iterable


class FarmerGame:
    """
    A class to represent a farmer's game.

    Attributes:
        itemNames (tuple[str, ...]): The names of the items in the game.
        badStates (set[State]): A set of states that are invalid.
        source (State): The starting state of the game.
        target (State): The target state of the game.
    """

    def __init__(
        self, itemNames: tuple[str, ...], badStates: Optional[Set[State]] = None
    ) -> None:
        """
        Initializes a Farmer's Game with the provided items and optionally defines bad states.

        This method sets up the game based on a tuple of `itemNames`, which represent the items involved in the game.
        The first item in the tuple is always the item (Farmer), that is required to cross the river with any other items.
        Additionally, a set of "bad" or forbidden states can be provided to specify configurations that are not allowed.

        Args:
            itemNames (tuple[str, ...]): A tuple of strings representing the names of the items in the game.
                The first item in the tuple is the farmer, who must always accompany other items during crossings.
            badStates (Optional[Set[State]], optional): A set of states that are considered illegal and should be avoided.
                Defaults to None if no bad states are specified.
        """

        self.itemNames = itemNames
        if not badStates:
            self.badStates: Set[State] = set()
        else:
            self.badStates = badStates
        self.source: Optional[State] = None
        self.target: Optional[State] = None

    def setSource(self, source: State) -> None:
        if source in self.badStates:
            raise ValueError("Source State is a bad State")
        else:
            self.source = source

    def setTarget(self, target: State) -> None:
        if target in self.badStates:
            raise ValueError("target State is a bad State")
        else:
            self.target = target

    def addBadStates(self, badStates: Iterable[State]) -> None:
        """
        Adds all states in the given Iterable to `badStates`.

        Args:
            badStates (Iterable[State]): Iterable of states to be added to the `badStates` attribute of `FarmerGame`.

        Raises:
            ValueError: If a state equal to the source state is attempted to be added.
            ValueError: If a state equal to the target state is attempted to be added.
        """
        for state in badStates:
            if state == self.source:
                raise ValueError(
                    f"Attempted to add state {state} which is the source state"
                )
            elif state == self.target:
                raise ValueError(
                    f"Attempted to add state {state} which is the target state"
                )
            self.badStates.add(state)

    def __backTrack(self, endState: State) -> tuple[List[State], bool]:
        """
        Private method to compute a path to the specified end state by tracing back through its predecessors.

        This method utilizes the `prev` attribute of `State` objects to reconstruct the sequence of states
        leading to the given `endState`, effectively creating a path from the starting state to the target.

        Args:
            endState (State): The state for which the path is to be computed, based on its successive predecessors.

        Returns:
            tuple(List[State], bool): A tuple where the first element is a list of `State` objects representing the
            path from the source to the target (if found), and the second element is a boolean indicating whether
            the path was successfully found. If no path exists, the return value defaults to ([], False).
        """

        path: List[State] = [endState]
        while endState.prev:
            path.append(endState.prev)
            endState = endState.prev
        return path[::-1], True

    def __movesFromPath(self, path: List[State]) -> None:
        """
        private method that returns the actions required to take for the given path using the following format:
        f"Move {rightMovedItems} right" or f"Move {leftMovedItems} left".

        Args:
            path (List[State]): list of states representing a path.

        Returns:
            None: this method does not return any value.
        """
        print(f"Actions required to reach State {self.target} from {self.source}:")

        for i in range(len(path) - 1):
            curr: State = path[i]
            next: State = path[i + 1]
            leftIdx: List[int] = []
            rightIdx: List[int] = []

            for idx, values in enumerate(zip(curr.itemsLeft, next.itemsLeft)):
                diff: int = int(values[1]) - int(values[0])
                if diff == 0:
                    continue
                elif diff == 1:
                    leftIdx.append(idx)
                elif diff == -1:
                    rightIdx.append(idx)

            leftMovedItems: str = ", ".join([curr.itemNames[idx] for idx in leftIdx])
            rightMovedItems: str = ", ".join([curr.itemNames[idx] for idx in rightIdx])
            if leftMovedItems:
                print(f"Move {leftMovedItems} left")
            elif rightMovedItems:
                print(f"move {rightMovedItems} right")

    def bfs(self, printActions: bool = False) -> tuple[List[State], bool]:
        """
        Performs a breadth-first search (BFS) to find a valid path from the source state to the target state.

        Args:
            printActions (bool, optional): If True, prints the sequence of actions required to go from the source state
                to the target state. Defaults to False.

        Raises:
            ValueError: If the source state is not specified.
            ValueError: If the target state is not specified.

        Returns:
            tuple(List[State], bool): A tuple where the first element is the list of states representing the path from
            the source to the target (if found), and the second element is a boolean indicating whether the search
            was successful. If no path is found, defaults to ([], False).

        """

        if not isinstance(self.source, State):
            raise ValueError("Source is not specified")
        if not isinstance(self.target, State):
            raise ValueError("Target is not specified")
        q: Deque[State] = deque()
        visited: Set[State] = set([self.source])
        q.append(self.source)

        while q:
            curr: State = q.popleft()
            if curr == self.target:
                path: List[State]
                succes: bool
                path, succes = self.__backTrack(curr)
                if printActions:
                    self.__movesFromPath(path)
                    return path, succes
                else:
                    return path, succes

            for neighbour in curr.getNeighbours():
                if neighbour not in visited:
                    if neighbour not in self.badStates:
                        visited.add(neighbour)
                        q.append(neighbour)

        return [], False
