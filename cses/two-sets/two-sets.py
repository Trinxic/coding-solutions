def two_sets(n: int) -> None:
    num_sum: int = int(n * (n + 1) / 2)

    if num_sum % 2 != 0:  # sets can't be equal -> (2 * k) must be even
        print("NO")
        return None
    num_sum = int(num_sum / 2)  # one half for each of the two sets

    i: int = 1
    j: int = n
    b_sum: int = 0
    a: list[int] = []
    b: list[int] = []

    while b_sum + j <= num_sum:
        b_sum += j
        b.append(j)
        j -= 1

    if last_b_num := num_sum - b_sum:
        b.append(last_b_num)

    while i <= j:
        if i != last_b_num:
            a.append(i)
        i += 1

    print("YES")
    print(f"{len(b)}\n{' '.join(str(x) for x in b)}")
    print(f"{len(a)}\n{' '.join(str(x) for x in a)}")

    return None


def main():
    two_sets(int(input()))


if __name__ == "__main__":
    main()
