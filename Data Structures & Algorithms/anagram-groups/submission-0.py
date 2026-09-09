class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dict/hashMap (val,ascii-num)
        # group each of the same value ascii within a List
        # return the list - easy peasy

        myMap = defaultdict(list)

        for s in strs:
            char_count = [0] * 26
            for char in s:
                val = ord(char) - ord('a')
                char_count[val] +=1

            freq_key = tuple(char_count)
            myMap[freq_key].append(s)

        return list(myMap.values())




        