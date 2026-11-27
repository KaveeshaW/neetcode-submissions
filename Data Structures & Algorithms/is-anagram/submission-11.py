class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for c in s:
            s_map[c] += 1
        
        for c in t:
            t_map[c] += 1
        
        if len(s_map) != len(t_map):
            return False

        for k, v in s_map.items():
            if v != t_map[k]:
                return False

        return True


