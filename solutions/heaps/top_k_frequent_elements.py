# Top K Frequent Elements (LC #347)
# URL: https://leetcode.com/problems/top-k-frequent-elements/
# ─────────────────────────────────────────
# DIFFICULTY : Medium
# PATTERN    : Heap
# APPROACH   : The solution first counts the frequency of each number using a hash map. Then, it iterates through the frequency map and maintains a min-heap of size k. If the heap size exceeds k, the least frequent element is removed. This ensures the heap always contains the k most frequent elements encountered so far.
# TIME       : O(n log k)
# SPACE      : O(n)
# ─────────────────────────────────────────
# KEY INSIGHT: A min-heap can be used to efficiently track the top k elements by storing (frequency, number) pairs and popping the minimum frequency element when the heap size exceeds k.
# GOTCHAS    : Ensure the heap stores frequency as the primary sorting key to correctly identify the least frequent elements. The final result should be the numbers, not their frequencies.
# ─────────────────────────────────────────
# RATING     : ⭐⭐⭐☆☆ (3/5)
# REVISIT    : 🔁 YES — add to revision list
# DATE       : 2026-06-16
# ─────────────────────────────────────────
# YOUR INSIGHT:
# use min heap to keep track of the top k and pop less-frequent

import heapq
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fmap = collections.Counter(nums)
        heap = []
        for num,freq in fmap.items():
            # push to min heap
            heapq.heappush(heap, (freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]
