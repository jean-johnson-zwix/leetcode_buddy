# Maximum Average Subarray I (LC #643)
# URL: https://leetcode.com/problems/maximum-average-subarray-i/
# ─────────────────────────────────────────
# DIFFICULTY : Easy
# PATTERN    : Sliding Window
# APPROACH   : This solution employs a fixed-size sliding window. It first calculates the sum of the initial `k` elements. Then, it slides the window across the array, updating the current sum by subtracting the element leaving the window and adding the new element entering, continuously tracking the maximum average encountered.
# TIME       : O(n)
# SPACE      : O(1)
# ─────────────────────────────────────────
# KEY INSIGHT: For fixed-length subarray problems, a sliding window efficiently calculates sums (or other aggregates) by incrementally updating the window's state (sum) in O(1) time per slide, avoiding recalculation for each subarray.
# GOTCHAS    : Remember to divide the current sum by `k` to get the average, not just the sum. Python handles floating-point division well, but in other languages, be mindful of potential precision issues.
# ─────────────────────────────────────────
# RATING     : ⭐⭐⭐☆☆ (3/5)
# REVISIT    : 🔁 YES — add to revision list
# DATE       : 2026-03-05
# ─────────────────────────────────────────
# YOUR INSIGHT:
# Fixed Length Sliding Window: initialize window, slide window by removing leftmost, adding rightmost

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # initialize window
        current_sum=0
        for i in range(0,k):
            current_sum+=nums[i]
        max_avg=current_sum/k
        # sliding my window
        for i in range(k,len(nums)):
            current_sum+=nums[i]-nums[i-k] # remove left, add right
            max_avg=max(max_avg,current_sum/k)
        return max_avg
