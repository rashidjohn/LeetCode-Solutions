"""
Problem: Climbing Stairs
URL: https://leetcode.com/problems/climbing-stairs
Description: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Difficulty: Easy
"""

def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    
    a = 1
    b = 2
    for i in range(3, n + 1):
        a, b = b, a + b

    return b

n = 3
print(climbStairs(n))

n = 8
print(climbStairs(n))