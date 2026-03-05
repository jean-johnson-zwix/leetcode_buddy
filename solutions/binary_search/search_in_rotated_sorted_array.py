# Search in Rotated Sorted Array (LC #33)
# URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
# ─────────────────────────────────────────
# DIFFICULTY : Medium
# PATTERN    : Binary Search
# APPROACH   : This solution employs a modified binary search algorithm. In each step, it identifies which half of the array (from `left` to `mid` or `mid` to `right`) is sorted. Based on the sorted half, it checks if the target value falls within that sorted range to narrow down the search space, otherwise, it searches the other half.
# TIME       : O(log n)
# SPACE      : O(1)
# ─────────────────────────────────────────
# KEY INSIGHT: The core idea is that in a rotated sorted array, at least one half (either `nums[left...mid]` or `nums[mid...right]`) will always be sorted. By identifying this sorted half, we can efficiently determine if the target is present in it or if we need to search the other, potentially unsorted, half.
# GOTCHAS    : Carefully handling the conditions for identifying the sorted half (`nums[left] <= nums[mid]`) and correctly updating the `left` and `right` pointers (`mid+1` or `mid-1`). Ensure the target range checks (`nums[left] <= target <= nums[mid]`) are precise.
# ─────────────────────────────────────────
# RATING     : ⭐⭐⭐☆☆ (3/5)
# REVISIT    : 🔁 YES — add to revision list
# DATE       : 2026-03-05
# ─────────────────────────────────────────
# YOUR INSIGHT:
# find which half is sorted by: nums[left]<=nums[mid] or not. after finding the sorted half, check if target is in the range of the half, else, update to next half

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]: #left half is sorted
                # check if target is in left half
                if nums[left]<=target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else: # right half is sorted
                # check if target is in right half
                if nums[mid]<=target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
