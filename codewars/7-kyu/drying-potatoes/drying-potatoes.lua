local kata = {}

function kata.potatoes(p0, w0, p1)
	-- dry_weight = ((100-p0)/100) * p0
	-- local dry_weight = (100 - p0) * w0

	-- old_weight = old_weight_water + dry_weight

	-- new_weight_water = p1 * new_weight
	-- new_weight = new_weight_water + dry_weight => new_weight_water = new_weight - dry_weight
	-- p1 * new_weight = new_weight - dry_weight
	-- (p1 - 1) * new_weight = - dry_weight
	-- new_weight = (-dry_weight) / (p1 - 1)
	-- new_weight = dry_weight / (1 - p1)

	-- removed the percentage (p1/100 => p1) since the cancel out in the final equation anyway
	-- local new_weight = dry_weight / (1 - p1)
	-- change: 1 - p1/100 => 100 - p1

	return math.floor(((100 - p0) * w0) / (100 - p1))
end

-- Define the main function
local function main()
	print("should be 50  | result: " .. kata.potatoes(99, 100, 98))
	print("should be 114 | result: " .. kata.potatoes(82, 127, 80))
	print("should be 100 | result: " .. kata.potatoes(93, 129, 91))
end

-- using lua
if arg and debug.getinfo(1, "S").source:sub(2) == arg[0] then
	main()
end

return kata
