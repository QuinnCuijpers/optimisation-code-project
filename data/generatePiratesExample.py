from itertools import product
from copy import deepcopy

itemNames: list[str] = ["Captain"]

numberPirates = 3
for i in range(numberPirates):
    itemNames += [f"Pirate{i}"]

numberOfGold = 5
for i in range(numberOfGold):
    itemNames += [f"Gold{i}"]

with open("./data/piratesData.txt", "w") as file:
    file.write(" ".join(itemNames) + "\n")
    source: list[int] = [0 for _ in itemNames]
    target: list[int] = [1 for _ in itemNames]
    file.write(" ".join(map(str, source)) + "\n")
    file.write(" ".join(map(str, target)) + "\n")

# creates list of all possible states
perms = list(product([0, 1], repeat=1 + numberOfGold + numberPirates))

badStates: list[tuple] = []

# checks if a state is illegal
for perm in perms:
    piratesLeft: int = sum(perm[1 : numberPirates + 1])
    amountGoldLeft: int = sum(perm[1 + numberPirates : -1])
    # 2 or more pirates and a captain and less gold then pirates and captain combined,
    # this leads to a mutiny as the pirates outnumber the captain and the pirates dont have gold to keep them satisfied
    if piratesLeft >= 2 and perm[0] == 1 and amountGoldLeft < piratesLeft:
        badStates.append(deepcopy(perm))

with open("./data/piratesBadStates.txt", "w") as file:
    file.write(f"{len(badStates)}" + "\n")
    for badState in badStates:
        file.write(" ".join(map(str, badState)) + "\n")
