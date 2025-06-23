# time: 00:23:40

class Solution:
    def isPalindrome(self, s: str) -> bool:
        reference = ""

        for character in s: # O(n)
            if character.isalpha() or character.isdigit():
                reference += character.lower()

        check = "".join(list(reversed(reference))) # O(3n) -> O(n)

        for i in range(len(reference)): # O(n)
            if reference[i] != check[i]:
                return False

        return True

solver = Solution()

solver.isPalindrome("A man, a plan, a canal: Panama") == True
solver.isPalindrome("Hello, world!") == False
