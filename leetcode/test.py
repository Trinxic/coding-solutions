from icecream import ic

ic("hello")

lst = [-4, -1, -1, 0, 1, 2]

prev: int = None

for i in range(5):
    if i < prev:
        prev += i
    ic(i)
