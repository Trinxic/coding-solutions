def solve_palindrome(string: str) -> str:
    a_count: dict[str:int] = {}
    for letter in string:
        if letter in a_count:
            a_count[letter] += 1
        else:
            a_count[letter] = 1

    fixed_palindrome = []
    odd_found = False
    odd_letter = ""
    odd_letter_count = 0
    for key, value in a_count.items():
        if value % 2 != 0:
            if odd_found:
                return "NO SOLUTION"
            else:
                odd_found = True
                odd_letter = key
                odd_letter_count = value
        else:
            fixed_palindrome.append(key * (value // 2))

    return (
        "".join(fixed_palindrome)
        + (odd_letter * odd_letter_count)
        + "".join(fixed_palindrome[::-1])
    )


def main():
    print(solve_palindrome(input()))


if __name__ == "__main__":
    main()
