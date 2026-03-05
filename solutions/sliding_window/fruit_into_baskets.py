# Fruit Into Baskets (LC #904)
# URL: https://leetcode.com/problems/fruit-into-baskets/
# ─────────────────────────────────────────
# DIFFICULTY : Medium
# PATTERN    : Sliding Window
# APPROACH   : This solution uses a dynamic sliding window approach with a frequency map. The window expands to the right, adding fruits to the map. If the number of distinct fruit types in the window exceeds two, the window shrinks from the left, removing fruits until only two types remain. The maximum valid window size is tracked.
# TIME       : O(n)
# SPACE      : O(1)
# ─────────────────────────────────────────
# KEY INSIGHT: The problem can be rephrased as finding the longest subarray with at most two distinct elements, which is a classic application of the sliding window pattern.
# GOTCHAS    : Ensure to remove a fruit type from the frequency map only when its count drops to zero after decrementing. Update `max_count` only when the window is valid (i.e., `len(f_count) <= 2`).
# ─────────────────────────────────────────
# RATING     : ⭐⭐⭐⭐☆ (4/5)
# REVISIT    : ✅ No
# DATE       : 2026-03-05
# ─────────────────────────────────────────
# YOUR INSIGHT:
# Dynamic window sliding with frequency map: add new fruits to frequency map, shrink window while len of frequency map greater than 2. Track max_count

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        max_count=0
        # frequency map
        f_count={}
        # start expanding
        for right in range(0,len(fruits)):
            # add fruit to basket
            if fruits[right] in f_count:
                f_count[fruits[right]]=f_count.get(fruits[right])+1
            else:
                f_count[fruits[right]]=1
            # check if window is valid
            while len(f_count) > 2:
                # take fruit out
                f_count[fruits[left]]=f_count.get(fruits[left])-1
                if f_count[fruits[left]]==0:
                    del f_count[fruits[left]]
                left+=1
            # window is valid now
            max_count=max(max_count, right-left+1)
        return max_count
