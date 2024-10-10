from typing import Optional, List


class State:
    itemNames: tuple[str, ...] = tuple("Itemnames not set")

    def __init__(self, itemsLeft: List[bool], prev: Optional["State"] = None):
        self.itemsLeft = itemsLeft
        self.prev = prev

    @classmethod
    def addItemNames(cls, itemNames: tuple[str, ...]):
        cls.itemNames = itemNames

    def __str__(self) -> str:
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

    def __hash__(self):
        # This allows the state to be used in a set or as a dictionary key
        return hash(tuple(self.itemsLeft))

    def getNeighbours(self) -> List["State"]:

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
