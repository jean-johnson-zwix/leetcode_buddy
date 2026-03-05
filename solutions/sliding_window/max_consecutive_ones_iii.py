# Max Consecutive Ones III (LC #1004)
# URL: https://leetcode.com/problems/max-consecutive-ones-iii/
# ─────────────────────────────────────────
# DIFFICULTY : Medium
# PATTERN    : Sliding Window
# APPROACH   : This solution employs a two-pointer sliding window technique. The `right` pointer expands the window, incrementing a `zero_count` when a zero is encountered. If `zero_count` exceeds `k`, the `left` pointer shrinks the window, decrementing `zero_count` if the element at `left` was a zero, until the window becomes valid again. The maximum valid window length is tracked throughout the process.
# TIME       : O(n)
# SPACE      : O(1)
# ─────────────────────────────────────────
# KEY INSIGHT: The core idea is to maintain a sliding window that always contains at most `k` zeros. Expand the window as much as possible, and shrink it from the left only when the `k` zero constraint is violated.
# GOTCHAS    : Ensure `max_len` is updated *after* the window has been made valid (i.e., `zero_count <= k`). Correctly decrement `zero_count` only when the element being removed from the left is a zero.
# ─────────────────────────────────────────
# RATING     : ⭐⭐⭐⭐☆ (4/5)
# REVISIT    : ✅ No
# DATE       : 2026-03-05
# ─────────────────────────────────────────
# YOUR INSIGHT:
# Dynamic Window Sliding pattern: shrink window while zero_count is invalid

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        max_len=0
        zero_count=0
        # start expanding
        for right in range(0,len(nums)):
            if nums[right]==0:
                zero_count+=1
            # if window is not valid
            while zero_count>k:
                # keep shrinking
                if nums[left]==0:
                    zero_count-=1
                left+=1
            # window is valid now
            max_len=max(max_len,right-left+1)
        
        return max_len
