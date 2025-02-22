def is_divisible(*nums):
    if not nums:
        return False
    if len(nums) < 2:
        return True
    first: int = nums[0]
    for num in nums[1:]:
        if first % num != 0:
            return False
    return True


def main():
    print(is_divisible(100, 25, 10, 5, 4))


if __name__ == "__main__":
    main()
