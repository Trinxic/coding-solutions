# @leet start
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        ans: int = 0
        # num_cars: int = len(position)
        time_left: list[int] = [
            (target - pos) / spd
            for pos, spd in sorted(zip(position, speed), reverse=True)
        ]
        slowest: int = float("-inf")
        for time in time_left:
            if time > slowest:
                slowest = time
                ans += 1
        return ans
# @leet end

"""
 * dist. to target => target - position[i]
 * time to target  => (target - position[i]) / speed[i]
 If time is equal or less than car after it, they will become a fleet
 Go in reverse order.

speed:
           T
         2
       4
1
    1
  3
           T

*time:
           T
         1
       1
12
    7
  3
           T

"""
