def number_of_moves(n: int, nums: list[int]):
    if n < 2:
        return 0

    moves = 0
    for i in range(1, n):
        if nums[i] >= nums[i - 1]:
            continue
        moves += nums[i - 1] - nums[i]
        nums[i] = nums[i - 1]

    return moves


def main():
    n: int = int(input())
    nums: list[int] = [int(x) for x in input().split()]
    print(number_of_moves(n, nums))


if __name__ == "__main__":
    main()
