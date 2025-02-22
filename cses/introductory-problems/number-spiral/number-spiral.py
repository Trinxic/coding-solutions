def locate_num(y: int, x: int) -> int:
    if y >= x:
        if y % 2 == 0:
            return y**2 - x + 1
        else:
            return (y - 1) ** 2 + x

    if x % 2 != 0:
        return x**2 - y + 1

    return (x - 1) ** 2 + y


def main():
    for _ in range(int(input())):
        y, x = (int(n) for n in input().split())
        print(locate_num(y, x))


if __name__ == "__main__":
    main()
