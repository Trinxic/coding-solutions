def difference_of_squares(n: int) -> int:
    return int(((n * (n + 1) / 2) ** 2) - (1 / 6 * n * (n + 1) * (2 * n + 1)))


def main():
    print(difference_of_squares(5))
    print(difference_of_squares(10))
    print(difference_of_squares(100))


if __name__ == "__main__":
    main()
