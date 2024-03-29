# -*- coding: utf-8 -*-
"""Two Sum II.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UFYFG4l-qZC6H1GhwLgroNnGp8P7B7xB

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.



Example 1:

Input: numbers = [2,7,11,15], target = 9

Output: [1,2]

Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6

Output: [1,3]

Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1

Output: [1,2]

Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

class Solution:
    def twoSum(numbers, target):

        sol = {}

        for index,value in enumerate(numbers):

            temp = target - value

            if temp in sol:
                a = [sol[temp], index]
                a = list(map(lambda x: x + 1, a))

                return a

            else:
                sol[value] = index

        return []

numbers = [2,7,11,15]
target = 9

Solution.twoSum(numbers, target)

"""Here's a step-by-step explanation of the logic:

1. **Initialization**:
   - `sol` is initialized as an empty dictionary. This dictionary will store the numbers encountered so far and their corresponding indices.

2. **Main Loop**:
   - The loop iterates through each element in `numbers` along with its index using the `enumerate` function.
   - For each element `value` in `numbers`, it calculates the complementary value `temp` needed to reach the target by subtracting `value` from `target`.

3. **Checking Complementary Value**:
   - It checks if the complementary value `temp` exists in the dictionary `sol`.
   - If `temp` exists in `sol`, it means the current `value` and the complementary value found earlier sum up to the target.
   - In this case, it creates a list `a` containing the indices of the two numbers. Then, it increments each index by 1 using `map(lambda x: x + 1, a)` to convert from 0-based to 1-based indexing.
   - Finally, it returns the list `a` containing the indices.

4. **Storing Values**:
   - If the complementary value is not found in `sol`, it means the current value does not yet have a complementary value to reach the target.
   - So, it stores the current value `value` and its index `index` in the dictionary `sol`.

5. **Returning Solution**:
   - If the loop finishes without finding a solution, it returns an empty list, indicating that no two numbers in `numbers` sum up to the target.

This solution efficiently finds the indices of the two numbers that sum up to the target using a dictionary to store encountered numbers and their indices. If a solution is found, it returns a list containing the indices with 1-based indexing.
"""