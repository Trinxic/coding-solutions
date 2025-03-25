# @leet start
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        temps_len: int = len(temperatures)
        days: list[int] = [0] * temps_len

        # stack: list[(int, int)] = []
        for i, temp in enumerate(reversed(temperatures[:-1])):
            next_ind = temps_len - i - 1
            if temp < temperatures[next_ind]:
                days[next_ind - 1] = 1
            elif temp == temperatures[next_ind]:
                days[next_ind - 1] = days[next_ind] and days[next_ind] + 1
            else:
                day_sum = days[next_ind] + 1
                while temp >= temperatures[next_ind - 1 + day_sum]:
                    if (additional_days := days[next_ind - 1 + day_sum]) == 0:
                        day_sum = 0
                        break
                    day_sum += additional_days
                days[next_ind - 1] = day_sum
        return days
# @leet end
