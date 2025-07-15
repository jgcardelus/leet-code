class Solution:
    def compareVersion(self, version1, version2):
        def to_version_list(version):
            version_list = []
            for revision in version.split("."):
                version_list.append(int(revision))

            return version_list

        def get_revision(version_list, i):
            if i < len(version_list):
                return version_list[i]
            return 0

        version1 = to_version_list(version1)
        version2 = to_version_list(version2)

        max_length = max(len(version1), len(version2))
        i = 0

        while i < max_length:
            revision1 = get_revision(version1,i)
            revision2 = get_revision(version2,i)

            if revision1 == revision2:
                i+=1
                continue

            if revision1 < revision2:
                return -1
            else:
                return 1

        return 0

solver = Solution()
print(solver.compareVersion("1.0", "1.0.0.0"))
print(solver.compareVersion("1.2", "1.10"))
