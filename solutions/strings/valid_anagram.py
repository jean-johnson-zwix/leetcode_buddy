# Valid Anagram (LC #242)
# URL: https://neetcode.io/problems/is-anagram/
# ─────────────────────────────────────────
# DIFFICULTY : Easy
# PATTERN    : HashMap
# APPROACH   : To determine if two strings are anagrams, we can count the frequency of each character in both strings. If the character counts are identical for both strings, then they are anagrams.
# TIME       : O(n)
# SPACE      : O(n)
# ─────────────────────────────────────────
# KEY INSIGHT: Anagrams have the exact same character counts.
# GOTCHAS    : Ensure that the lengths of the strings are the same. If they are not, they cannot be anagrams. Case sensitivity might be a consideration depending on the problem constraints, but for this problem, it's assumed to be case-sensitive.
# ─────────────────────────────────────────
# RATING     : ⭐⭐⭐⭐⭐ (5/5)
# REVISIT    : ✅ No
# DATE       : 2026-06-15
# ─────────────────────────────────────────
# YOUR INSIGHT:
# find the frequency map for both strings and compare

import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
