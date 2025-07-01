class Solution:
    def findSubstring(self, s, words):
        length = len(words[0])

        solutions = []

        right = 0
        left = 0

        while left < len(s):
            current_window = s[left:left+length]
            print(current_window)
            if current_window not in words:
                left += 1
                continue

            words.remove(current_window)
            removed = [current_window]

            # Current window IS in words
            right = left + length
            while right + length <= len(s):
                next_window = s[right:right+length]
                if next_window not in words:
                    break

                removed.append(next_window)
                words.remove(next_window)

                if len(words) == 0:
                    solutions.append(left)
                    break

                right += length

            words.extend(removed)
            left += 1

        return solutions

solver = Solution()
print(solver.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
