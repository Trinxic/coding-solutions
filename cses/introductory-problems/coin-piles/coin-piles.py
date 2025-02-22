def removeable_coin_piles(a: int, b: int) -> str:
    if a == 0 or b == 0:
        return "YES" if a == b else "NO"
    if max([a, b]) / 2 <= min([a, b]):
        return "YES" if (a + b) % 3 == 0 else "NO"
    return "NO"


def main():
    for _ in range(int(input())):
        piles: list[int] = [int(x) for x in input().split()]
        print(removeable_coin_piles(piles[0], piles[1]))


if __name__ == "__main__":
    main()
