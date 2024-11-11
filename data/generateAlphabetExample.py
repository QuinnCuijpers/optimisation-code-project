consts = "bcdfg"
vowels = "aeiou"
symbols = "!@#$%"

# noinspection DuplicatedCode
with open("./data/alphabetData.txt", "w") as file:
    names: str = " ".join([const for const in consts])
    names = names + " " + " ".join([vowel for vowel in vowels])
    names = names + " " + " ".join([symbol for symbol in symbols])
    file.write(names + "\n")

    letters = consts + vowels + symbols
    source: list[int] = [0 for _ in letters]
    target: list[int] = [1 for _ in letters]

    file.write(" ".join(map(str, source)) + "\n")
    file.write(" ".join(map(str, target)) + "\n")


with open("./data/alphabetBadStates.txt", "w") as file:
    file.write(f"{2*len(vowels)*(len(consts) - 1)*len(symbols)}" + "\n")
    for i, const in enumerate(consts):
        for j, vowel in enumerate(vowels):
            j += len(consts)
            for k, symbol in enumerate(symbols):
                if i == 0:
                    continue
                k += len(consts) + len(vowels)

                stateLeft: list[int] = [
                    0 for _ in range(len(consts) + len(vowels) + len(symbols))
                ]
                stateRight: list[int] = [
                    1 for _ in range(len(consts) + len(vowels) + len(symbols))
                ]

                stateLeft[i], stateLeft[j], stateLeft[k] = (
                    int(not stateLeft[i]),
                    int(not stateLeft[j]),
                    int(not stateLeft[k]),
                )
                stateRight[i], stateRight[j], stateRight[k] = (
                    int(not stateRight[i]),
                    int(not stateRight[j]),
                    int(not stateRight[k]),
                )
                file.write(" ".join(map(str, stateLeft)) + "\n")
                file.write(" ".join(map(str, stateRight)) + "\n")
