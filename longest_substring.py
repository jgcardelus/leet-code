class Solution:
    def lengthOfLongestSubstring(self, s):
        longest = 0
        left = 0
        found = set()

        for right in range(len(s)):
            letter = s[right]
            if letter not in found:
                found.add(letter)
                longest = max(longest, len(found))
                continue

            # A letter HAS been found
            while letter in found:
                tail = s[left]
                found.remove(tail)
                left += 1

            found.add(letter)

        return longest

solver = Solution()
print(solver.lengthOfLongestSubstring(""))
