# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

def maxProfit(prices: list[int]) -> int:
    maxProfit = 0
    l, r = 0, 1
    while r < len(prices):
        profit = prices[r] - prices[l]
        if profit < 0:
            l, r = r, r+1
        else:
            maxProfit = max(profit, maxProfit)
            r = r+1
    return maxProfit

prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
print(maxProfit(prices2))