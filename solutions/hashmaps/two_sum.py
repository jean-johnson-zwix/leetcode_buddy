# Two Sum (LC #1)
# URL: https://leetcode.com/problems/two-sum/
# ─────────────────────────────────────────
# DIFFICULTY : Easy
# PATTERN    : HashMap
# APPROACH   : The solution iterates through the array once, using a hash map (dictionary in Python) to store each number encountered along with its index. For each number, it calculates the 'complement' needed to reach the target. If this complement is already present in the hash map, it means the pair has been found, and their respective indices are returned. Otherwise, the current number and its index are added to the hash map for future lookups.
# TIME       : O(n)
# SPACE      : O(n)
# ─────────────────────────────────────────
# KEY INSIGHT: Utilizing a hash map to store previously seen numbers and their indices allows for constant time (average) lookup of the required complement, transforming an O(n^2) brute-force approach into an efficient O(n) solution.
# GOTCHAS    : Ensure the hash map stores the value as the key and the index as the value. The order of operations is crucial: check for the complement *before* adding the current element to the hash map to correctly handle cases where the complement is the current element itself (e.g., target = 6, nums = [3,3]).
# ─────────────────────────────────────────
# RATING     : ⭐⭐⭐⭐⭐ (5/5)
# REVISIT    : ✅ No
# DATE       : 2026-02-23
# ─────────────────────────────────────────
# YOUR INSIGHT:
# avoid inner loop by adding a hash map to store {value:index}

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            nums[i] + nums[j] = target
            output: [i, j]
            run 1: 
                [2,7,11,15], 9
                initialize: {}
                2 -> 9-2 = 7 -> {2:0}
                7 -> 9-7 = 2 -> {2:0} -> return 0
            run 2: 
                [3,2,4], 6
                initialize: {}
                3 -> 6-3 -> 3 -> {3:0}
                2 -> 6-2 -> 4 -> {3:0, 2:1}
                4 -> 6-4 -> 2 -> return [1,2]
        '''
        element_dir = {}
        for i in range(0,len(nums)):
            required_element = target - nums[i]
            if required_element in element_dir:
                return [element_dir[required_element], i]
            else:
                element_dir[nums[i]] = i
