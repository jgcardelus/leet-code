class Solution:
    def hash_str(self, str):
        return "".join(sorted(str))

    def groupAnagrams(self, strs):
        anagrams = {}
        for str in strs:
            str_hash = self.hash_str(str)
            if str_hash in anagrams.keys():
                anagrams[str_hash].append(str)
            else:
                anagrams[str_hash] = [str]

        return list(anagrams.values())
