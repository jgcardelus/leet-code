class Solution:
    def flipgame(self, fronts, backs):
        impossible = set()
        deck = []

        for f,b in zip(fronts, backs):
            if f == b:
                impossible.add(f)
            deck.extend([f,b])

        deck.sort()
        good = 0

        for number in deck:
            if number in impossible:
                continue

            good = number
            break

        return good

solver = Solution()
print(solver.flipgame([1,2],[1,1]))
