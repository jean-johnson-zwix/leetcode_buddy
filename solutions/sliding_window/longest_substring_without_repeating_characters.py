# Longest Substring Without Repeating Characters (LC #3)
# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=plakya4j
# ─────────────────────────────────────────
# DIFFICULTY : Medium
# PATTERN    : Sliding Window
# APPROACH   : This solution employs a dynamic sliding window with two pointers, `left` and `right`. The `right` pointer expands the window, adding characters to a hash set. If a duplicate character is found, the `left` pointer shrinks the window by removing characters from the set until the duplicate is no longer present, ensuring the window always contains unique characters. The maximum valid window length is tracked throughout the process.
# TIME       : O(n)
# SPACE      : O(min(n, A))
# ─────────────────────────────────────────
# KEY INSIGHT: The efficiency stems from using a hash set for O(1) average-time duplicate checks and a two-pointer sliding window to dynamically adjust the substring, avoiding redundant character re-scans.
# GOTCHAS    : Ensure the window size calculation `right - left + 1` is correct. Handle edge cases like an empty string, a string with all identical characters, or a string with all unique characters.
# ─────────────────────────────────────────
# RATING     : ⭐⭐⭐☆☆ (3/5)
# REVISIT    : 🔁 YES — add to revision list
# DATE       : 2026-03-05
# ─────────────────────────────────────────
# YOUR INSIGHT:
# Dynamic Sliding Window: right pointer to expand window, left pointer to shrink window to avoid duplicate, hashset to track duplicate

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        max_len=0
        left=0
        # expand window
        for right in range(0,len(s)):
            # shrink window if duplicate
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            max_len=max(max_len, right-left+1)
        return max_len
