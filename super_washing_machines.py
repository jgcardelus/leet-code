# Greedy
# Busque max, min
#   Pase 1 del max al min
# Repita


class Solution:
    def find_min_number(self, washing_machines):
        if sum(washing_machines) % len(washing_machines) != 0:
            return -1

        def find_max(washing_machines):
            max_index = 0
            max_number = -1

            for i, n in enumerate(washing_machines):
                if n > max_number:
                    max_number = n
                    max_index = i

            return max_index, max_number

        def find_min(washing_machines, max):
            min_index = -1
            min_number = max

            for i, n in enumerate(washing_machines):
                if n < min_number:
                    min_number = n
                    min_index = i

            return min_index, min_number

        # Solution when find_min and max are the same
        steps = 0

        last_max_number = find_max(washing_machines)
        iterations_on_max_number = 0

        while True:
            max_index, max_number = find_max(washing_machines)
            min_index, min_number = find_min(washing_machines, max_number)

            if last_max_number != max_number:
                iterations_on_max_number = 0
            else:
                iterations_on_max_number += 1

            if max_number == min_number:
                return steps

            steps += abs(max_index - min_index)
            washing_machines[max_index] -= 1
            washing_machines[min_index] += 1

solver = Solution()
print(solver.find_min_number([1,0,5]))
print(solver.find_min_number([0,3,0]))
print(solver.find_min_number([0,2,0]))
