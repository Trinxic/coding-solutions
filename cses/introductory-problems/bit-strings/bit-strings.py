def bit_combinations(n: int) -> int:
    return 2**n % (10**9 + 7)


def main():
    print(bit_combinations(int(input())))


if __name__ == "__main__":
    main()
