# Best Time to Buy and Sell Stock (LC #121)
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# ─────────────────────────────────────────
# DIFFICULTY : Easy
# PATTERN    : Greedy
# APPROACH   : The solution iterates through the `prices` array once. It maintains two variables: `min_price` to track the lowest buying price encountered so far, and `max_profit` to store the maximum profit found. For each price, it updates `min_price` if a lower price is found, otherwise it calculates the potential profit with the current `min_price` and updates `max_profit`.
# TIME       : O(n)
# SPACE      : O(1)
# ─────────────────────────────────────────
# KEY INSIGHT: To maximize profit, always track the minimum buying price encountered up to the current day and calculate the potential profit with the current day's price.
# GOTCHAS    : Ensure to handle cases where no profit can be made (e.g., prices are strictly decreasing), in which case the profit should be 0. An empty or single-element input array should also result in 0 profit.
# ─────────────────────────────────────────
# RATING     : ⭐⭐⭐⭐⭐ (5/5)
# REVISIT    : ✅ No
# DATE       : 2026-02-23
# ─────────────────────────────────────────
# YOUR INSIGHT:
# keep the min sell price fixed and parse through the array to find a lower sell price or higher profit

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        Strategy:
        [7,1,5,3,6,4] -> day 1 price = 7, day 2 price = 1, and so on
        profit = sell price - cost price -> goal is to maximize the price -> minimize the sell price
        track sell price, max_profit
        """
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
