class Solution {
    public boolean canPartition(int[] nums) {
        int sum1 = Arrays.stream(nums).sum();
        if (sum1 % 2 != 0) {
            return false;
        }
        int len1 = nums.length;
        int target = sum1 / 2;
        Boolean[][] dp = new Boolean[len1][target + 1];
        for (int i = 0; i < len1; i++){
            dp[i][0] = true;
        }
        for (int j = 1; j < target+1; j++){
            dp[0][j] = nums[0] == j ? true : false;
        }
        for (int i = 1; i < len1; i++){
            for (int j = 1; j < target+1; j++){
                if (dp[i-1][j] == true) {
                    dp[i][j] = dp[i-1][j];
                } else if (j > nums[i]) {
                    dp[i][j] = dp[i-1][j-nums[i]];
                } else {
                    dp[i][j] = false;
                }
            }
        }
        return dp[len1-1][target];
    }
}