<<<<<<< HEAD
=======
test: dict[str : list[int, int]] = {}

s: str = " "

for i, letter in enumerate(s):
    print(f"i: {i} | letter: {letter}")
    if letter in test:
        print("letter already exists")
    else:
        test[letter] = [1, i]

for key, value in test.items():
    print(f"key: <<{key}>> | value[0]: {value[0]}")

letter_test = ""
print(letter_test)
>>>>>>> e8a5b4c (Added some solutions (some may be a work-in-progress).)
