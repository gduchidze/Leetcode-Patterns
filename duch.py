from typing import List

# #121. Best Time to Buy and Sell Stock
# def maxProfit(prices: List[int]) -> int:
#     min_price = float('inf')  # პირველი Breakpoint
#     max_profit = 0
#
#     for price in prices:  # მეორე Breakpoint
#         profit = price - min_price
#         min_price = min(price, min_price)
#         max_profit = max(profit, max_profit)
#         print(f"Price: {price}, Min Price: {min_price}, Profit: {profit}, Max Profit: {max_profit}")
#     return max_profit
#
# # ტესტი Debug რეჟიმისთვის
# prices = [7, 1, 5, 3, 6, 4]
# maxProfit(prices)
#


# class Solution:
#     def findClosestNumber(self, nums: List[int]) -> int:
#         closest = nums[0]
#         for x in nums:
#             if abs(x) < abs(closest):
#                 closest = x
        
#         if closest < 0 and abs(closest) in nums:
#             return abs(closest)
#         else:
#             return closest
# Time: O(n)
# Space: O(1)

# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         A, B = len(word1), len(word2)
#         a, b = 0, 0
#         s = []
#         word = 1
#
#         print(f"Initial lengths -> word1: {A}, word2: {B}")
#
#         while a < A and b < B:
#             if word == 1:
#                 print(f"Appending {word1[a]} from word1")
#                 s.append(word1[a])
#                 a += 1
#                 word = 2
#             else:
#                 print(f"Appending {word2[b]} from word2")
#                 s.append(word2[b])
#                 b += 1
#                 word = 1
#             print(f"Current state of s: {''.join(s)}")
#
#         while a < A:
#             print(f"Appending remaining {word1[a]} from word1")
#             s.append(word1[a])
#             a += 1
#             print(f"Current state of s: {''.join(s)}")
#
#         while b < B:
#             print(f"Appending remaining {word2[b]} from word2")
#             s.append(word2[b])
#             b += 1
#             print(f"Current state of s: {''.join(s)}")
#
#         result = ''.join(s)
#         print(f"Final merged string: {result}")
#         return result
#
# # Example usage:
# solution = Solution()
# solution.mergeAlternately("abc", "defg")


