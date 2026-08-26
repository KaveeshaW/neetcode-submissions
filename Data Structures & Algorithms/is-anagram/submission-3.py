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

        sDictionary = {}
        tDictionary = {}

        if(len(s) != len(t)):
            return False

        for letter in s:
            if letter in sDictionary:
                sDictionary[letter] += 1
            else:
                sDictionary[letter] = 1
            
        for letter in t:
            if letter in tDictionary:
                tDictionary[letter] += 1
            else:
                tDictionary[letter] = 1

        for key, value in sDictionary.items():
            if(tDictionary.get(key) != value):
                return False

        return True


