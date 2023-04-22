class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict={}
        i = 0
        max_len=0

        for j in range(len(s)):
            if s[j] in char_dict:
                i = max(i,char_dict[s[j]]+1)
            char_dict[s[j]] = j
            max_len = max(max_len, j - i + 1)

        return max_len