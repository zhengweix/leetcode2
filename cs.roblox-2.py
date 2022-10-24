class Solution:
    '''
    You are given an array of integers numbers. Return the difference between the sum of all even-positioned elements with values between -100 to 100 (inclusive of both ends) and the sum of all odd-positioned elements with values that lie within the same range.
    Assume that array indices are 0-based.

    Example
    For numbers = [101, 3, 4, 359, 2, 5], the output should be solution(numbers) = -2.
    Sum of even-positioned elements with values within the range of [-100; 100] is numbers[2] + numbers[4] = 4 + 2 = 6 (numbers[0] = 101 is filtered out).
    Sum of odd-positioned elements with values within the range of [-100; 100] is numbers[1] + numbers[5] = 3 + 5 = 8 (numbers[3] = 359 is filtered out).
    6 - 8 = -2, so the expected output is -2.
    For numbers = [-2, 234, 100, 99, 540, -1], the output should be solution(numbers) = 0.

    Sum of even-positioned elements within the range of [-100; 100] is numbers[0] + numbers[2] = (-2) + 100 = 98 (numbers[4] = 540 is filtered out).
    Sum of odd-positioned elements within the range of [-100; 100] is numbers[3] + numbers[5] = 99 + (-1) = 98 (numbers[1] = 234 is filtered out).
    98 - 98 = 0, so the expected output is 0.
    For numbers = [-9], the output should be solution(numbers) = -9.

    The only even-positioned element is -9, which is within the range of [-100, 100].
    There are no odd-positioned elements, so the sum is 0.
    -9 - 0 = -9, so the expected output is -9.
    Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer numbers
    An array of integers.

    Guaranteed constraints:
    1 ≤ numbers.length ≤ 103,
    -103 ≤ numbers[i] ≤ 103.

    [output] integer
    The difference between sums described above.

    Input:
numbers: [101, 3, 4, 359, 2, 5]
Expected Output:
-2

Input:
numbers: [-2, 234, 100, 99, 540, -1]
Expected Output:
0

Input:
numbers: [-9]
Expected Output:
-9

Input:
numbers: [10, 240, 140, 40, 34]
Expected Output:
4

Input:
numbers: [101, -101, -101, 1]
Expected Output:
-1

Input:
numbers: [85, 75, 96, -62, -34]
Expected Output:
134

Input:
numbers: [145, 125, -149, -33, 93]
Expected Output:
126

Input:
numbers: [-8, -9, -9, -8, -2, -10, -10, 9, 9, -2]
Expected Output:
0

Input:
numbers: [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected Output:
-10

Input:
numbers: [101, -101, 0, 1, -101, 101]
Expected Output:
-1
    '''
    def solution(numbers):

