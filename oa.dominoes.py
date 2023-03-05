from itertools import *
class Solution:
    '''
    John found six dominoes. A domino is a rectangular tile with a line dividing its face into two square halves. Each half is marked with a number of spots. John wants to build a three-stage pyramid from these dominoes. The first level should consist of three dominoes, the second level of two dominoes and the highest of one domino. The levels are arranged in such a way that the peak of the pyramid is at the center: that is, each level is positioned over the center of the level below it. There is also an additional condition. The number of spots on each domino half should be the same as the number of spots on the half positioned beneath it. Note that this does not apply to neighboring dominoes on the same level.

    Is it possible to build a pyramid from these dominoes, as described above? Dominoes can be freely rearranged. We also assume that dominoes can be rotated (that is, the piece [X, Y] can be treated as [X, Y] or [Y, X], where X denotes the number of spots in the first half-domino and Y denotes the number of spots in the second half-domino).

    Write a function: func Solution(A []int) string that, given an array A consisting of twelve integers (the first and the second integer describe the first domino, the third and the fourth integer describe the second domino, etc.), returns the string "YES", if it is possible to build a correct pyramid from these dominoes or "NO" otherwise. For example, given:

    A = [4, 3, 3, 4, 1, 2, 2, 3, 6, 5, 4, 5] the function should return "YES". John found the following dominoes: [4, 3], [3, 4], [1, 2], [2, 3], [6, 5], [4, 5]. There are several ways to build the pyramid. For instance, John can rotate first and fifth domino and as a result gets: [3, 4], [3, 4], [1, 2], [2, 3], [5, 6], [4, 5]. Next, he can place the third, the first and the fifth domino at the first level (in this order), the fourth and the sixth domino at the second level (also in this order) and the second domino at the highest level. The result will be:
    https://codility-frontend-prod.s3.amazonaws.com/media/task_static/domino_pyramid/static/images/auto/12213f2e66ae904990adbed075bf04ca.png

    Assume that:
    array A contains twelve integers; each element of array A is an integer within the range [1..12].
    '''
    @staticmethod
    def dominoes(A):
        def helper1(arr):
            '''Check each permutation if it can build a correct pyramid'''
            return arr[0] == arr[3] and arr[1] == arr[4] and arr[2] == arr[7] and arr[3] == arr[8] and arr[4] == arr[9] and arr[5] == arr[10]

        for perm in permutations(A):
            '''Generate permutations of domino faces'''
            if helper1(perm):
                return 'YES'
        return 'NO'

print(Solution.dominoes([4, 3, 3, 4, 1, 2, 2, 3, 6, 5, 4, 5]))



