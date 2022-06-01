class Solution {
    public int findKthPositive(int[] arr, int k) {
        int num = 1;
        int miss = 0;
        int i = 0;
        int n = arr.length;
        while (i < n) {
            if (arr[i] != num) {
                miss += 1;
                if (miss == k) {
                    return num;
                }
            } else {
                i += 1;
            }
            num += 1;
        }
        return arr[n-1] + k - miss;
    }
}