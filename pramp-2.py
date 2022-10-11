class FindDuplicates:
    '''
    Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers
    that are both in arr1 and arr2.

    Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions:
      M ≈ N - the array lengths are approximately the same
      M ≫ N - arr2 is much bigger than arr1.

    input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]
    output: [3, 6, 7]
    '''
    #! Note that the output array should be sorted in an ascending order.
    # tc: O(m+n) sc: O(m+n)
    def find_duplicates(self1, arr1, arr2):
        return sorted(list(set(arr1) & set(arr2)))

    # tc: O(m+n) sc: O(n)
    def find_duplicates1(self, arr1, arr2):
        i, j = 0, 0
        ans = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] == arr2[j]:
                ans.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1
        return ans

    # tc: O(nlogm) sc: O(n)
    def find_duplicates2(self, arr1, arr2):
        def helper(arr, target):
            left, right = 0, len(arr)-1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    return True
            return False

        if arr2 < arr1:
            arr1, arr2 = arr2, arr1

        ans = []
        for n in arr1:
            if helper(arr2, n):
                ans.append(n)
        return ans

    def main(self):
        print(self.find_duplicates([10,20,30,40,50,60,70,80], [10,20,30,40,50,60]))

S = FindDuplicates()
S.main()