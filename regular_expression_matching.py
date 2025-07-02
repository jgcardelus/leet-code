# 2 arrays
#   - Palbara
#   - Match
#
# Por cada letra
#   - compruebo si es . or char, que se válido
#          - si no, false
#           - si, me guardo last-match
#
#   - si un *
#       - compruebo que actual (no sea) o sea igual a last match
#       - si lo es, guardo last match

class Solution:
    def match_regex(self, word, regex):
        last_match = None

        i = 0
        j = 0

        # aaaaaaab
        # a*b

        while i < len(regex) and j < len(word):
            lookup = regex[i]

            if lookup != "*":
                if lookup == "." or lookup == word[j]:
                    if lookup == ".":
                        last_match = "."
                    else:
                        last_match = word[j]
                    i += 1
                    j += 1
                    continue

                return False
            else:
                while j < len(word) and last_match is not None:
                    if word[j] != word[last_match]:
                        break

                    j += 1

                i += 1

        if j < len(word):
            return False

        return True

solver = Solution()
print(solver.match_regex("aa", "a"))
print(solver.match_regex("aa", "a."))
print(solver.match_regex("aa", "a*"))
print(solver.match_regex("b", "a*"))
print(solver.match_regex("aaaaaaaaab", "a*b"))
# print(solver.match_regex("", "a*b"))
