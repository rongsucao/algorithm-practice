class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0
        subarry = {}
        ans = 0
        for i, str in enumerate(s):
            if str not in subarry:
                subarry[str] = i
                ans = max(ans, i + 1 -left)
            else:
                left = subarry.get(str) + 1
                subarry = {}
                for j in range(left, i+1):
                    subarry[s[j]] = j
                subarry[str] = i
        
        return ans