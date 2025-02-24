local function difference_of_squares(n)
	local square_of_nums = ((n * (n + 1)) / 2) ^ 2
	local square_of_squares = (1 / 6) * n * (n + 1) * ((2 * n) + 1)
	return square_of_nums - square_of_squares
end

-- Define the main function
local function main()
	print(difference_of_squares(5))
	print(difference_of_squares(25))
end

-- using lua
if arg and debug.getinfo(1, "S").source:sub(2) == arg[0] then
	main()
end
