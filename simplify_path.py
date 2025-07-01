class Solution:
    def get_route(self, path):
        directories = path.split("/")
        chunks = []
        for directory in directories:
            if directory == "":
                chunks.append("/")
            else:
                chunks.append(directory)
                chunks.append("/")

        return chunks

    def simplifyPath(self, path):
        simplified_path = []
        route = self.get_route(path)

        for direction in route:
            if direction == "..":
                simplified_path.pop()
                if len(simplified_path)>0:
                    simplified_path.pop()
            elif direction == ".":
                continue
            elif direction == "/" and len(simplified_path) > 0:
                if simplified_path[-1] == "/":
                    continue
                else:
                    simplified_path.append("/")
            else:
                simplified_path.append(direction)

        if len(simplified_path) > 1 and simplified_path[-1] == "/":
            simplified_path.pop()

        return "".join(simplified_path)


solver = Solution()
print(solver.simplifyPath("/home/"))
print(solver.simplifyPath("/home//foo/"))
print(solver.simplifyPath("/home/user/Documents/../Pictures"))
print(solver.simplifyPath("/../"))
print(solver.simplifyPath("/.../a/../b/c/../d/./"))
