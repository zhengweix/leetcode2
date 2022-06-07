class Solution {
    public int maxSubArray(int[] nums) {
        int sum1 = nums[0];
        int sum2 = 0;
        for (int num : nums) {
            if (sum2 > 0) {
                sum2 = num;
            } else {
                sum2 += num;
            }
            sum1 = max(sum1, sum2);
        }
        return sum1;
    }
}