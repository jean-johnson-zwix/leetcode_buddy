# Longest Consecutive Sequence (LC #128)
# URL: https://leetcode.com/problems/longest-consecutive-sequence/
# ─────────────────────────────────────────
# DIFFICULTY : Medium
# PATTERN    : HashMap
# APPROACH   : The solution first converts the input list into a hash set for efficient O(1) average time lookups. It then iterates through each number in the set, only initiating a sequence count if the current number `n` is the true start of a sequence (i.e., `n-1` is not present in the set). From this starting point, it iteratively checks for consecutive numbers (`n+1`, `n+2`, etc.) in the set, extending the current sequence length until a gap is found, and updates the maximum length found so far.
# TIME       : O(n)
# SPACE      : O(n)
# ─────────────────────────────────────────
# KEY INSIGHT: To achieve O(N) time complexity, only start counting a sequence from its true beginning. This is identified by checking if `n-1` does not exist in the set, preventing redundant checks for numbers already known to be part of an ongoing sequence.
# GOTCHAS    : Forgetting to use a hash set for O(1) lookups can lead to an O(N^2) solution. Not handling duplicates (though the set naturally does this).
# ─────────────────────────────────────────
# RATING     : ⭐⭐⭐☆☆ (3/5)
# REVISIT    : 🔁 YES — add to revision list
# DATE       : 2026-02-26
# ─────────────────────────────────────────
# YOUR INSIGHT:
# find the last element of a sequence if the n is not already in nums_set

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums) # for O(1) lookup
        longest_sequence_length = 0
        for n in nums_set:
            if (n-1) not in nums_set:
                last_element_of_sequence = n
                current_sequence_length = 1
                while (last_element_of_sequence+1) in nums_set:
                    last_element_of_sequence+=1
                    current_sequence_length+=1
                longest_sequence_length = max(longest_sequence_length, current_sequence_length)
        return longest_sequence_length
