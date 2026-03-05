# 3Sum (LC #15)
# URL: https://leetcode.com/problems/3sum/
# ─────────────────────────────────────────
# DIFFICULTY : Medium
# PATTERN    : Two Pointer
# APPROACH   : The array is first sorted to enable the two-pointer technique. An outer loop iterates through each element, fixing it as the first number. For the remaining elements, two pointers (left and right) are used to find two numbers that sum to the negative of the fixed number. Duplicate triplets are avoided by skipping over identical elements during iteration and pointer movement.
# TIME       : O(n^2)
# SPACE      : O(n)
# ─────────────────────────────────────────
# KEY INSIGHT: Sorting the array is crucial as it allows for the efficient two-pointer approach and simplifies the logic for skipping duplicate elements to ensure unique triplets.
# GOTCHAS    : The primary challenge is correctly handling duplicates for all three elements (the fixed element, and both two-pointer elements) to prevent adding identical triplets to the result. This requires checks like `if i > 0 and nums[i] == nums[i-1]: continue` and similar checks within the two-pointer loop.
# ─────────────────────────────────────────
# RATING     : ⭐⭐☆☆☆ (2/5)
# REVISIT    : 🔁 YES — add to revision list
# DATE       : 2026-03-05
# ─────────────────────────────────────────
# YOUR INSIGHT:
# Two Pointer: sort array to enable two pointer. use for loop to fix one element and two pointer for the other two. the tricky part is skipping duplicates. since array is sorted, skip if current element same as previous element for both num[i], num[left] and num[right]

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result=[]
        for i in range(0,len(nums)):
            # skip duplicates
            if i>0 and nums[i]==nums[i-1]:
                continue
            # two pointer
            left=i+1 # second element
            right=len(nums)-1 # second last element
            while left<right:
                current_sum = nums[i]+nums[left]+nums[right]
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    #skip duplicates
                    while left<right and nums[left]==nums[left-1]: left+=1
                    while left<right and nums[right]==nums[right+1]: right-=1
                elif current_sum<0: left+=1
                else: right-=1
        return result
