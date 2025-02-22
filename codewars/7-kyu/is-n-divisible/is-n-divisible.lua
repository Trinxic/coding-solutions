local solution = {}

function solution.isDivisible(first, ...)
	if first == nil then
		return false
	end

	for _, num in ipairs({ ... }) do
		if first % num ~= 0 then
			return false
		end
	end

	return true
end

-- Define the main function
local function main()
	print(solution.isDivisible(12, 3, 4)) -- true
	print(solution.isDivisible(12, 5, 4)) -- false
end

-- using luajit
-- if arg[0]:match("is%-n%-divisible/is%-n%-divisible.lua$") then
-- 	main()
-- end

-- using lua
if debug.getinfo(1, "S").source == arg[0] then
	main()
end

return solution
