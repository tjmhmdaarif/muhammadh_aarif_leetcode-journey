class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30,  31, 30, 31, 31, 30, 31, 30, 31]

        def date_to_day (date_str: str) -> int:
            month, day = map(int, date_str.split('-'))
            return sum(days_in_months[:month - 1]) + day
        
        a_start = date_to_day (arriveAlice)
        a_end = date_to_day(leaveAlice)
        b_start = date_to_day(arriveBob)
        b_end = date_to_day (leaveBob)

        start = max(a_start, b_start)
        end = min(a_end, b_end)

        return max(0, end - start + 1)