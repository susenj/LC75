'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Solution:
___________

loop through the price list.
Set the minPrice and maxProfit.
First price can be taken as minimum price to start with.
Compare each element with the minPrice and set the minPrice.
If next element is lesser than minPrice - it's a loss situation...so we don't carry on to see the profit.
rather, we just continue the loop and go to the next element.

if next element is greater than the minPrice and also greater than the previous price, then only we should add up the profit.
prices[i] - minPrice should be greater than the maxProfit set so far. 

Example: 3,2,6,5,0,3

even though, 2-6 is profit 4
next profit is from 0-3, which is 3 only. and 3 is not greater than 4.


    int minPrice=Integer.MAX_VALUE,sell=0;
        for(int i=0;i<prices.length;i++){
            minPrice=Math.min(minPrice,prices[i]);
            sell=Math.max(sell,prices[i]-minPrice);
        }
    return sell;

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''Brute-Force Approach
        maxProfit = 0
        if len(prices) == 1:
            return 0
        
        for i in range(0, len(prices)-1):
            diff = 0
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    temp = prices[j] - prices[i]
                    if temp > diff:
                        diff = temp
            if diff > maxProfit:
                maxProfit = diff
        return maxProfit'''
        
        # One-pass approach
        maxProfit = 0
        minPrice = 100001
        for i in range(0, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
                continue
            if (prices[i] > prices[i-1]) and ((prices[i] - minPrice) > maxProfit):
                maxProfit = prices[i] - minPrice
                                
        return maxProfit   
