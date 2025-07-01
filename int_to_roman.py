from collections import deque


class Solution:
    def intToRoman(self, num):
        to_roman = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

        def append_units(digit, power):
            nonlocal to_roman

            roman = ""
            unit = to_roman[10**power]

            for i in range(digit):
                roman += unit

            return roman

        digits = deque([char for char in str(num)])
        roman = ""
        while digits:
            digit = int(digits.popleft())
            power = len(digits)

            if digit == 9:
                next_power = to_roman[10**(power+1)]
                one_less = to_roman[10**power]
                roman += one_less + next_power
            elif 9 > digit >= 5:
                five_in_power = to_roman[5*10**power]
                roman += five_in_power + append_units(digit - 5, power)
            elif digit == 4:
                five_in_power = to_roman[5*10**power]
                one_less = to_roman[10**power]
                roman += one_less + five_in_power
            else:
                roman += append_units(digit, power)

        return roman

solver = Solution()
print(solver.intToRoman(3749))
