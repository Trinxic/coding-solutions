def weird_algo(n: int) -> None:
    print(n)
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        print(int(n))


def main():
    weird_algo(int(input()))


if __name__ == "__main__":
    main()
