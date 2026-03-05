# Binary Search (LC #704)
# URL: https://leetcode.com/problems/binary-search/
# ─────────────────────────────────────────
# DIFFICULTY : Easy
# PATTERN    : Binary Search
# APPROACH   : This problem uses the classic iterative binary search algorithm on a sorted array. Pointers `left` and `right` define the current search space, and `mid` is calculated to divide this space. The search space is halved in each iteration until the target is found or the pointers cross.
# TIME       : O(log n)
# SPACE      : O(1)
# ─────────────────────────────────────────
# KEY INSIGHT: The core idea of binary search is to repeatedly divide the search interval in half, eliminating a large portion of the array in each step, which is only possible on a sorted array.
# GOTCHAS    : Ensure the `mid` calculation `left + (right - left) // 2` prevents integer overflow (though less critical in Python). Correctly adjust `left = mid + 1` and `right = mid - 1` to avoid infinite loops and ensure the entire search space is covered. The loop condition `while left <= right` is crucial for handling single-element arrays and ensuring the target is checked if it's at `mid` when `left == right`.
# ─────────────────────────────────────────
# RATING     : ⭐⭐⭐⭐☆ (4/5)
# REVISIT    : ✅ No
# DATE       : 2026-03-05
# ─────────────────────────────────────────
# YOUR INSIGHT:
# Binary Search: calculate mid using left+(right-left)//2 and based on nums[mid], search left half or right half

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target: # search left
                left=mid+1
            if nums[mid]>target: # search right
                right=mid-1
        return -1
