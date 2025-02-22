def find_trailing_zeros(n: int) -> int:
    # #of0 = n/5 + n/25 + n/125 + ...
    count = 0
    po5 = 5
    while n // po5 != 0:
        count += n // po5
        po5 *= 5
    return count


def main():
    print(find_trailing_zeros(int(input())))


if __name__ == "__main__":
    main()
