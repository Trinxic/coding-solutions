def repetitions(dna: str) -> int:
    max_rep: int = 0
    curr_rep: int = 0
    prev_char: str = dna[0]

    for character in dna:
        if prev_char == character:
            curr_rep += 1
        else:
            if max_rep < curr_rep:
                max_rep = curr_rep
            curr_rep = 1
        prev_char = character

    if max_rep < curr_rep:
        max_rep = curr_rep

    return max_rep


def main():
    print(repetitions(input()))


if __name__ == "__main__":
    main()
