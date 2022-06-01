package com.leetcode;

class Solution {
    public static double findMaxAverage(int[] nums, int k) {
        double result = -Double.MAX_VALUE;
        double winSum = 0.0;
        int winStart = 0;
        for(int winEnd=0; winEnd < nums.length; winEnd++) {
            winSum += nums[winEnd];
            if(winEnd >= k-1){
                result = Math.max(result, winSum/k);
                winSum -= nums[winStart];
                winStart += 1;
            }
        }
        return result;
    }
}
