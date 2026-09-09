class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}

        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
            # If the char exists inside the hashMap it will increatments by 1 if not defualt to the num 0
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1
            
        # return a bool if both are the same 
        return freq_t == freq_s
        