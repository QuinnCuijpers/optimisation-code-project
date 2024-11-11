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
        self, item_names: tuple[str, ...], bad_states: Optional[Set[State]] = None
    ) -> None:
        """
        Initializes a Farmer's Game with the provided items and optionally defines bad states.

        This method sets up the game based on a tuple of `item_names`, which represent the items involved in the game.
        The first item in the tuple is always the item (Farmer), that is required to cross the river with any other items.
        Additionally, a set of "bad" or forbidden states can be provided to specify configurations that are not allowed.

        Args:
            item_names (tuple[str, ...]): A tuple of strings representing the names of the items in the game.
                The first item in the tuple is the farmer, who must always accompany other items during crossings.
            bad_states (Optional[Set[State]], optional): A set of states that are considered illegal and should be avoided.
                Defaults to None if no bad states are specified.
        """

        self.itemNames: tuple[str, ...] = item_names
        if not bad_states:
            self.badStates: Set[State] = set()
        else:
            self.badStates = bad_states
        self.source: Optional[State] = None
        self.target: Optional[State] = None

    def set_source(self, source: State) -> None:
        if self.badStates is not None:
            if source in self.badStates:
                raise ValueError("Source State is a bad State")
            else:
                self.source = source
        else:
            self.source = source

    def set_target(self, target: State) -> None:
        if self.badStates is not None:
            if target in self.badStates:
                raise ValueError("Source State is a bad State")
            else:
                self.target = target
        else:
            self.target = target

    def add_bad_states(self, bad_states: Iterable[State]) -> None:
        """
        Adds all states in the given Iterable to `bad_states`.

        Args:
            bad_states (Iterable[State]): Iterable of states to be added to the `bad_states` attribute of `FarmerGame`.

        Raises:
            ValueError: If a state equal to the source state is attempted to be added.
            ValueError: If a state equal to the target state is attempted to be added.
        """
        for state in bad_states:
            if state == self.source:
                raise ValueError(
                    f"Attempted to add state {state} which is the source state"
                )
            elif state == self.target:
                raise ValueError(
                    f"Attempted to add state {state} which is the target state"
                )
            self.badStates.add(state)

    @staticmethod
    def __back_track(end_state: State) -> tuple[List[State], bool]:
        """
        Private method to compute a path to the specified end state by tracing back through its predecessors.

        This method utilizes the `prev` attribute of `State` objects to reconstruct the sequence of states
        leading to the given `endState`, effectively creating a path from the starting state to the target.

        Args:
            end_state (State): The state for which the path is to be computed, based on its successive predecessors.

        Returns:
            tuple(List[State], bool): A tuple where the first element is a list of `State` objects representing the
            path from the source to the target (if found), and the second element is a boolean indicating whether
            the path was successfully found. If no path exists, the return value defaults to ([], False).
        """

        path: List[State] = [end_state]
        while end_state.prev:
            path.append(end_state.prev)
            end_state = end_state.prev
        return path[::-1], True

    def __moves_from_path(self, path: List[State]) -> None:
        """
        private method that returns the actions required to take for the given path using the following format:
        f"Move {right_moved_items} right" or f"Move {left_moved_items} left".

        Args:
            path (List[State]): list of states representing a path.

        Returns:
            None: this method does not return any value.
        """
        print(f"Actions required to reach State {self.target} from {self.source}:")

        for i in range(len(path) - 1):
            curr: State = path[i]
            next_state: State = path[i + 1]
            left_idx: List[int] = []
            right_idx: List[int] = []

            for idx, values in enumerate(zip(curr.items_left, next_state.items_left)):
                diff: int = int(values[1]) - int(values[0])
                if diff == 0:
                    continue
                elif diff == 1:
                    left_idx.append(idx)
                elif diff == -1:
                    right_idx.append(idx)

            left_moved_items: str = ", ".join([curr.item_names[idx] for idx in left_idx])
            right_moved_items: str = ", ".join([curr.item_names[idx] for idx in right_idx])
            if left_moved_items:
                print(f"Move {left_moved_items} left")
            elif right_moved_items:
                print(f"move {right_moved_items} right")

    def bfs(self, print_actions: bool = False) -> tuple[List[State], bool]:
        """
        Performs a breadth-first search (BFS) to find a valid path from the source state to the target state.

        Args:
            print_actions (bool, optional): If True, prints the sequence of actions required to go from the source state
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
        visited: Set[State] = {self.source}
        q.append(self.source)

        while q:
            curr: State = q.popleft()
            if curr == self.target:
                path: List[State]
                success: bool
                path, success = self.__back_track(curr)
                if print_actions:
                    self.__moves_from_path(path)
                    return path, success
                else:
                    return path, success

            for neighbour in curr.get_neighbours():
                if neighbour not in visited:
                    if neighbour not in self.badStates:
                        visited.add(neighbour)
                        q.append(neighbour)

        return [], False
