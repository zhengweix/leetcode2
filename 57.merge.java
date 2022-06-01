package com.leetcode;

class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> result = new ArrayList<>();
        Arrays.sort(intervals, (x, y) -> Integer.compare(x[0], y[0]));
        int[] current = intervals[0];
        for (int i = 1; i < intervals.length; i++) {
            int[] interval = intervals[i];
            if (current[1] >= interval[0]) {
                current = new int[] {current[0], Math.max(current[1], interval[1])};
            } else {
                result.add(current);
                current = interval;
            }
        }
        result.add(current);
        return result.toArray(new int[result.size()][]);
    }
}