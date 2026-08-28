class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for letter in s:
                count[ord(letter) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())
