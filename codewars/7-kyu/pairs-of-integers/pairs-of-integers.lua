local function generate_pairs(m, n)
	local result = {}
	for i = m, n do
		for j = i, n do
			table.insert(result, { i, j })
		end
	end
	return result
end

-- Define the main function
local function main()
	for _, pair in ipairs(generate_pairs(2, 4)) do
		print(pair[1], pair[2])
	end
end

-- using lua
if arg and debug.getinfo(1, "S").source:sub(2) == arg[0] then
	main()
end
