def safe_knights(k: int) -> int:
    # `k`: grid width/height
    total_combinations: int = (k**2) * (k**2 - 1)
    bad_combinations: int = 8 * (k - 2) * (k - 1)
    return int((total_combinations - bad_combinations) / 2)


def main():
    for k in range(1, int(input()) + 1):
        print(safe_knights(k))


if __name__ == "__main__":
    main()
