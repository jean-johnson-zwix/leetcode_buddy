# Pattern Reference

A running log of every problem solved, organized by pattern.

| Problem | Pattern | Key Insight | Time | Space | Rating |
|---------|---------|-------------|------|-------|--------|
| Two Sum (#1) | HashMap | Store value→index; look up complement | O(n) | O(n) | ⭐⭐⭐⭐⭐ |
| Best Time to Buy and Sell Stock (#121) | Greedy | Track min price seen so far and update max profit | O(n) | O(1) | ⭐⭐⭐⭐⭐ |
| Longest Consecutive Sequence (#128) | HashMap | Use a hash set to store numbers; only start sequence count if n-1 not present | O(n) | O(n) | ⭐⭐⭐ |
| Maximum Average Subarray I (#643) | Sliding Window | Fixed-size window; update sum by subtracting old, adding new; track max average | O(n) | O(1) | ⭐⭐⭐ |
| Longest Substring Without Repeating Characters (#3) | Sliding Window | Use a hash set to track characters in a dynamic window; shrink from left if duplicate | O(n) | O(min(n, A)) | ⭐⭐⭐ |
| Find All Anagrams in a String (#438) | Sliding Window, HashMap | Fixed-size window with frequency maps for anagram check | O(N) | O(1) | ⭐⭐⭐ |
| Max Consecutive Ones III (#1004) | Sliding Window | Maintain window with at most k zeros; expand right, shrink left if invalid | O(n) | O(1) | ⭐⭐⭐⭐ |
| Fruit Into Baskets (#904) | Sliding Window | Find longest subarray with at most 2 distinct elements using a frequency map | O(n) | O(1) | ⭐⭐⭐⭐ |
| Path Sum (#112) | DFS | Recursively subtract node value from target sum; check for zero at leaf | O(N) | O(H) | ⭐⭐⭐⭐ |
| Binary Search (#704) | Binary Search | Iteratively halve search space; adjust left/right pointers | O(log n) | O(1) | ⭐⭐⭐⭐ |
| Search in Rotated Sorted Array (#33) | Binary Search | Modified binary search; identify sorted half, then check target range | O(log n) | O(1) | ⭐⭐⭐ |
| Diameter of Binary Tree (#543) | DFS | Use a helper to return depth; track max diameter as `left_depth + right_depth` | O(n) | O(n) | ⭐⭐⭐ |
| Balanced Binary Tree (#110) | DFS | Recursively compute height and check balance at each node; use non-local flag for overall balance | O(N) | O(H) | ⭐⭐⭐ |
| First Bad Version (#278) | Binary Search | Find first true using `while left < right`, `right = mid` if true, `left = mid + 1` if false | O(log n) | O(1) | ⭐⭐⭐ |
| Two Sum II - Input Array Is Sorted (#167) | Two Pointer | Use two pointers from ends of sorted array; adjust based on sum vs target | O(n) | O(1) | ⭐⭐⭐⭐ |
| 3Sum (#15) | Two Pointer | Sort array, fix one element, use two pointers for the rest, handle duplicates carefully | O(n^2) | O(n) | ⭐⭐ |
