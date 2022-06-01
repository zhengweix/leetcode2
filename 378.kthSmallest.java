class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>((x, y) -> x - y);
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                minHeap.add(matrix[i][j]);
            }
        }
        for (int i = 0; i < k-1; i++) {
            minHeap.poll();
        }
        return minHeap.poll();
    }

    public int kthSmallest1(int[][] matrix, int k) {
        int n = matrix.length;
        int left = matrix[0][0];
        int right = matrix[n-1][n-1];
        while (left < right) {
            int mid = left + (right - left)/2;
            int count = helper1(matrix, mid, n, n);
            if (count < k) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return right;
    }
    public int helper1(int[][] matrix, int mid, int row, int col) {
        int i = row - 1;
        int j = 0;
        int count = 0;
        while (i >= 0 && j < col) {
            if (matrix[i][j] <= mid) {
                count += i + 1;
                j += 1;
            } else {
                i -= 1;
            }
        }
        return count;
    }
}