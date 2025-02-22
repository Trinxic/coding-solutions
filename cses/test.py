def main():
    # t_in = [0]
    # t_out = [1]
    # u_in = [2]
    file_text = [[], [], []]
    for i, filename in enumerate(
        ["test_input.txt", "test_output.txt", "user_output.txt"]
    ):
        with open(f"/Users/d.anderson/Downloads/{filename}", "r") as file:
            for line in file:
                file_text[i].append(line.strip())

    for n in range(99681):
        if file_text[1][n] != file_text[2][n]:
            print(
                f"test: {file_text[0][n]} | expected: {file_text[1][n]} | found: {file_text[2][n]}"
            )


if __name__ == "__main__":
    main()
