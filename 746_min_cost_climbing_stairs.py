'''
https://leetcode.com/problems/min-cost-climbing-stairs/
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

Solution:
_________
If we closely observe the first few examples by ourselves, we would see the trend of getting the minimal cost is same.
Get the minimum of next two steps and add it.
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ''' 
        # Working till 257 testcases; failed in [0,1,2,2]
        l = len(cost)
        def findCost(index, l, step, cost):
            i = index
            while (i < len(cost)):
                if (i+2 <= l-1) and (i+1 <= l-1):
                    if (cost[i+1] < cost[i+2]):
                        step += cost[i+1]
                        i += 1
                    else:
                        step += cost[i+2]
                        i += 2
                else:
                    i += 1
                print (i, step)
            return step
        # Find the cost if started at index 0
        step = cost[0]
        total0 = findCost(0, l, step, cost)

        # Find the cost if started at index 1
        step = cost[1]
        total1 = findCost(1, l, step, cost)

        if total0 < total1:
            return total0
        else:
            return total1
        '''
        # Easier solution: Credit: https://leetcode.com/jiaruy
        dp = cost + [0]
        for i in range(2, len(dp)):
            dp[i] += min(dp[i-2], dp[i-1])
        return dp[-1]
