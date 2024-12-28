from itertools import permutations

def solve_crypt_arithmetic(puzzle):
    word1, word2, result = puzzle
    letters = set(word1 + word2 + result)
    if len(letters) > 10:
        raise ValueError("Too many unique letters (more than 10).")

    solutions = []
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if mapping[word1[0]] == 0 or mapping[word2[0]] == 0 or mapping[result[0]] == 0:
            continue

        num1 = int("".join(str(mapping[ch]) for ch in word1))
        num2 = int("".join(str(mapping[ch]) for ch in word2))
        num_result = int("".join(str(mapping[ch]) for ch in result))

        if num1 + num2 == num_result:
            solutions.append(mapping)

    return solutions

if __name__ == "__main__":
    puzzle = ("SEND", "MORE", "MONEY")

    solutions = solve_crypt_arithmetic(puzzle)

    if solutions:
        print(f"Solutions for the puzzle {puzzle[0]} + {puzzle[1]} = {puzzle[2]}:")
        for solution in solutions:
            print(solution)
    else:
        print(f"No solutions found for the puzzle {puzzle[0]} + {puzzle[1]} = {puzzle[2]}.")
