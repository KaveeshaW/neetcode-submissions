class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create two dictionaries
        # go through the first one and get the number of times it each letter appears
        #     add to the first dictionary
        # go through the second one and get the number of times it each letter appears
        #     add to the second dictionary
        # compare the two dictionaries to see that each letter has the same count and return the value of the compare

        # time complexity O(n + m)
        # space complexity O(n + m)

        # first check that the length of the two strings are the same
        #   if they are not return false
        # sort the two strings and store both into new variables
        # compare for each value that they are the same
        
        # time complexity O(nlogn + mlogm)
        # space complexity O(n + m)

        #loop through one
        # check if the second one has the letter

        sSorted = "".join(sorted(s))
        tSorted = "".join(sorted(t))

        return sSorted == tSorted
        # if(len(s) != len(t)):
        #     return False

        # sMap, tMap = {}, {}

        # for index in range(len(s)):
        #     sMap[s[index]] = sMap.get(s[index], 0) + 1
        #     tMap[t[index]] = tMap.get(t[index], 0) + 1

        # for key, value in sMap.items():
        #     if(tMap.get(key) != value):
        #         return False

        # return True


