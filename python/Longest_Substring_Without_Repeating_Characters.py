class Solution:
    def lengthOfLongestSubstring(self, s):
        char_index = {}
        left = 0
        ans = 0
        
        for i, c in enumerate(s):
            if c in char_index and char_index[c] > left:
                left = char_index[c] + 1
                
            char_index[c] = i
            ans = max(ans, i - left + 1)
            
        return ans