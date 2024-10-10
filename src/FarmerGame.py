from typing import List, Set, Optional, Deque
from .State import State
from collections import deque
from collections.abc import Iterable


class FarmerGame:

    def __init__(
        self, itemNames: tuple[str, ...], badStates: Optional[Set[State]] = None
    ) -> None:
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
        for State in badStates:
            self.badStates.add(State)

    def __backTrack(self, state: State) -> tuple[List[State], bool]:
        path: List[State] = [state]
        while state.prev:
            path.append(state.prev)
            state = state.prev
        return path[::-1], True

    def __movesFromPath(self, path: List[State]) -> tuple[List[State], bool]:
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

        return path, True

    def bfs(self, printActions: bool = False) -> tuple[List[State], bool]:

        if not isinstance(self.source, State):
            raise ValueError("Source is not specified")
        if not isinstance(self.target, State):
            raise ValueError("Target is not specified")
        q: Deque[State] = deque()
        visited: Set[State] = set([self.source])
        q.append(self.source)

        while q:
            curr: State = q.popleft()
            if curr.itemsLeft == self.target.itemsLeft:
                path: List[State]
                succes: bool
                path, succes = self.__backTrack(curr)
                if printActions:
                    return self.__movesFromPath(path)
                else:
                    return path, succes

            for neighbour in curr.getNeighbours():
                if neighbour not in visited:
                    if neighbour not in self.badStates:
                        visited.add(neighbour)
                        q.append(neighbour)

        return [], False
