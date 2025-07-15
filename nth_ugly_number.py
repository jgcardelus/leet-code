# Dynamic Programming
# 3 ptrs

class Solution:
    def nthUglyNumber(self, n):
        ugly_numbers = set([1])

        def is_ugly(number):
            nonlocal ugly_numbers

            prime_factors = [2,3,5]
            for factor in prime_factors:
                if number in ugly_numbers:
                    number = 1
                    break

                while number % factor == 0:
                    number /= factor
                    if number in ugly_numbers:
                        number = 1
                        break

                if number == 1:
                    break

            if number == 1:
                return True
            return False

        number = 1
        last_ugly_number = 1
        while len(ugly_numbers) < n:
            if is_ugly(number):
                ugly_numbers.add(number)
                last_ugly_number = number
            number += 1

        return last_ugly_number

solver = Solution()
print(solver.nthUglyNumber(10))
