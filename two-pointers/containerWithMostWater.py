# Brute Force

def maxArea(heights):
    res = 0

    for i in range(len(heights)):
        for j in range(i+1, len(heights)):
            res = max(res, min(heights[i], heights[j]) * (j - 1))
    return res


# Two Pointer Approach

def maxArea(heights):
    res = 0
    l = 0, r = len(heights) - 1

    while l < r:
        res = max(res, min(heights[l], heights[r]) * (r - l))

        
