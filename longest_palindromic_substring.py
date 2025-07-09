# A bit ugly, but right

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(s):
            for i in range(len(s)//2):
                if s[i] != s[len(s) - 1 - i]:
                    return False
            return True

        left = 0
        right = len(s) - 1

        longuest_palindrome = 0
        result = s[0]

        while left < len(s) and left < right:
            substring_is_palindrome = False
            if s[left] == s[right]:
                substring_is_palindrome = is_palindrome(s[left:right+1])

            if substring_is_palindrome and right - left > longuest_palindrome:
               longuest_palindrome = right - left
               result = s[left:right+1]

               right = len(s) - 1
               left += 1

               if right - left < longuest_palindrome:
                   break
            else:
                right -= 1
                if right == left:
                    left += 1
                    right = len(s)- 1

                    if right - left < longuest_palindrome:
                        break

        return result

solver = Solution()
print(solver.longestPalindrome("babadada"))
