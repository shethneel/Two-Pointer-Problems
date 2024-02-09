'''

Problem :

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Problem : Leetcode 11

'''

class Solution:
    def maxArea(height):
        l = 0
        r = len(height)-1
        area = 0

        while l < r:
            cur_area = min(height[l], height[r]) * (r-l)
            area = max(area, cur_area)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1

        return area

sol = Solution.maxArea(height=[1,8,6,2,5,4,8,3,7])

print (sol)

'''

Certainly! Let's break down the logic of the provided code:

1. **Class Definition**: 
    - The code begins by defining a class named `Solution`.
    - Inside this class, there's a method called `maxArea`.

2. **maxArea Method**:
    - The `maxArea` method takes a single argument, `height`, which presumably is a list representing the heights of the vertical lines.
    - Two pointers `l` and `r` are initialized at the start and end of the `height` list, respectively.
    - A variable `area` is initialized to store the maximum area found.
    - The method uses a while loop to iterate until the left pointer `l` is less than the right pointer `r`. This loop will terminate once the two pointers meet or cross each other.
    - Inside the loop:
        - It calculates the current area (`cur_area`) by taking the minimum height between the heights at indices `l` and `r` (since the height of the water is limited by the shorter of the two lines) and multiplying it by the width (`r - l`), which represents the distance between the two vertical lines.
        - Updates the `area` variable to store the maximum of the current area and the previously stored maximum area.
        - Moves the pointers inward:
            - If the height at index `l` is less than the height at index `r`, it means the next potential area could be larger if the left pointer is moved to the right. Thus, `l` is incremented.
            - If the height at index `l` is greater than or equal to the height at index `r`, it means the next potential area could be larger if the right pointer is moved to the left. Thus, `r` is decremented.

3. **Return Value**:
    - After the while loop finishes, the method returns the maximum area found.

4. **Execution**:
    - Outside the class definition, an instance of `Solution` is created (`sol`).
    - The `maxArea` method is called with the `height` list `[1,8,6,2,5,4,8,3,7]`.
    - The result returned by the `maxArea` method is stored in `sol`.
    - Finally, `sol` is printed, which represents the maximum area of water that can be contained by the container formed by the vertical lines.

This code effectively uses a two-pointer approach to find the maximum area of water that can be contained by the container formed by the vertical lines.

'''