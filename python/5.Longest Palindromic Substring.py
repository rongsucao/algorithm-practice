#
# @lc app=leetcode id=5 lang=python3
# @lcpr version=30306
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        res = ""
        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i, i+1)
            
            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        
        return res        
        
            
            
# @lc code=end



#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

