def permutations(n: int) -> str:
    if n == 1:
        return "1"
    if n == 2 or n == 3:
        return "NO SOLUTION"

    odds = []
    evens = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            evens.append(str(i))
        else:
            odds.append(str(i))

    return " ".join(evens + odds)


def main():
    print(permutations(int(input())))


if __name__ == "__main__":
    main()
