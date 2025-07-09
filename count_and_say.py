class Solution:
    def count_and_say(self, n):
        encoded = "1"
        counter = 1

        def encode(string):
            encoded = ""
            left, right = 0, 0

            while right < len(string):
                if string[right] == string[left]:
                    right += 1
                else:
                    encoded += str(right-left) + string[left]
                    left = right
                    right += 1

            encoded += str(right-left) + string[left]

            return encoded


        while counter < n:
            encoded = encode(encoded)
            counter += 1

        return encoded

solver = Solution()
print(solver.count_and_say(4))
print(solver.count_and_say(1))
