class Solution:
    def wordBreak(self, s: str, wordDict):
        def remove(s, i):
            if i >= len(wordDict):
                return False

            s = s.replace(wordDict[i], " ")
            if s.strip() == "":
                return True

            return opt(s, i+1)

        def dont_remove(s,i):
            if i >= len(wordDict):
                return False

            return opt(s,i+1)

        def opt(s, i):
            print(s,i)
            return remove(s,i) or dont_remove(s,i)

        return opt(s,0)

solver = Solution()
print(solver.wordBreak("cbca", ["bc", "ca"]))
