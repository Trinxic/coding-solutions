def find_missing_number(n: int, nums: list[int]) -> int:
    return int(n * (n + 1) / 2 - sum(nums))


def main():
    n = int(input())
    nums = [int(n) for n in input().split()]
    print(find_missing_number(n, nums))


if __name__ == "__main__":
    main()
