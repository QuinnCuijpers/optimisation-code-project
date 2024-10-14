consts = "bcdfghjklm"
vowels = "aeiou"

with open("./data/alphabetData.txt", "w") as file:
    names = " ".join([const for const in consts])
    names = names + " " + " ".join([vowel for vowel in vowels])
    file.write(names + "\n")

    letters = consts + vowels
    source = [0 for _ in range(len(consts))] + [1 for _ in range(len(vowels))]
    target = [1 for letter in letters]

    file.write(" ".join(map(str, source)) + "\n")
    file.write(" ".join(map(str, target)) + "\n")


with open("./data/alphabetBadStates.txt", "w") as file:
    file.write(f"{2*len(vowels)*(len(consts) - 1)}" + "\n")
    for i, const in enumerate(consts):
        for j, vowel in enumerate(vowels):
            if i == 0:
                continue
            j += len(consts)
            stateLeft = [0 for _ in range(len(consts) + len(vowels))]
            stateRight = [1 for _ in range(len(consts) + len(vowels))]
            stateLeft[i], stateLeft[j] = int(not stateLeft[i]), int(not stateLeft[j])
            stateRight[i], stateRight[j] = int(not stateRight[i]), int(
                not stateRight[j]
            )
            file.write(" ".join(map(str, stateLeft)) + "\n")
            file.write(" ".join(map(str, stateRight)) + "\n")
