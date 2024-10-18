from typing import Optional, List


class State:
    """
    Represents a state in the Farmer's Game where certain items are either on the left or right side of the river.

    Each state keeps track of the items' positions (whether they are on the left side or not) and a reference
    to the previous state, allowing for backtracking during the search for a solution.

    Attributes:
        itemNames (tuple[str, ...]): A class-level attribute that stores the names of the items involved in the game.
            It is initialized with a default value of "Itemnames not set" and can be updated using the `addItemNames` method.
        itemsLeft (List[bool]): A list of boolean values indicating the position of each item.
            `True` means the item is on the left side, and `False` means it is on the right.
        prev (Optional[State]): A reference to the previous state, allowing the construction of a path through the states.
    """

    itemNames: tuple[str, ...] = tuple("Itemnames not set")

    def __init__(self, itemsLeft: List[bool], prev: Optional["State"] = None):
        """
        Creates a `State` object representing the positions of items based on a list of booleans.

        Each boolean value indicates whether a specific item is on the left side (`True`) or not (`False`).
        Optionally, a reference to the previous `State` can be provided to enable backtracking.

        Args:
            itemsLeft (List[bool]): A list of booleans where `True` represents the item being on the left side,
                and `False` represents the item being on the right side.
            prev (Optional["State"], optional): A reference to the previous `State` object, useful for backtracking through states.
                Defaults to None.
        """
        self.itemsLeft: List[bool] = itemsLeft
        self.prev: State | None = prev

    @classmethod
    def addItemNames(cls, itemNames: tuple[str, ...]) -> None:
        """
        Sets the names of the items for the `State` class.

        This class method allows the assignment of item names to the class-level attribute `itemNames`.
        These names are used to describe each item in the state representation of the game.

        Args:
            itemNames (tuple[str, ...]): A tuple containing the names of the items. The length of this tuple should match the
                number of items in the game (or the number of boolean values in the `itemsLeft` attribute of each `State`).

        """
        cls.itemNames = itemNames

    def __str__(self) -> str:
        if self.itemNames == tuple("Itemnames not set"):
            return "State without names"
        return (
            "["
            + ", ".join(
                [
                    self.itemNames[i]
                    for i in range(len(self.itemNames))
                    if self.itemsLeft[i]
                ]
            )
            + "]"
        )

    def __eq__(self, other) -> bool:
        if isinstance(other, State):
            return self.itemsLeft == other.itemsLeft
        return False

    def __hash__(self) -> int:
        # This allows the state to be used in a set or as a dictionary key
        return hash(tuple(self.itemsLeft))

    def getNeighbours(self) -> List["State"]:
        """
        Finds all neighboring states based on the current state's configuration.

        A neighboring state is one where:
        - Either only the first item (farmer) moves from one side to the other, or
        - The first item (farmer) moves together with an item from the same side.

        Returns:
            List[State]: A list of neighboring states derived from the current state.
        """
        neighbours: List[State] = []
        prev: State = self

        # farmer is on the right
        if not self.itemsLeft[0]:
            self.itemsLeft[0] = True
            neighbour = State(self.itemsLeft.copy(), prev)
            neighbours.append(neighbour)

            for i in range(1, len(self.itemsLeft)):
                if not self.itemsLeft[i]:
                    self.itemsLeft[i] = True
                    neighbour = State(self.itemsLeft.copy(), prev)
                    neighbours.append(neighbour)
                    self.itemsLeft[i] = False
            self.itemsLeft[0] = False

        # farmer is on the left
        if self.itemsLeft[0]:
            self.itemsLeft[0] = False
            neighbour = State(self.itemsLeft.copy(), prev)
            neighbours.append(neighbour)

            for i in range(1, len(self.itemsLeft)):
                if self.itemsLeft[i]:
                    self.itemsLeft[i] = False
                    neighbour = State(self.itemsLeft.copy(), prev)
                    neighbours.append(neighbour)
                    self.itemsLeft[i] = True
            self.itemsLeft[0] = True

        return neighbours