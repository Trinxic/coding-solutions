n: int = int(input("Max integer: "))
nums_list: list[str] = input("Nums: ").split()

# sum(1 to n) - sum(nums_list) = missing number
print(int(n * (n + 1) / 2 - sum([int(n) for n in nums_list])))
