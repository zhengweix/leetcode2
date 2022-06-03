class Solution {
    public int subarraySum(int[] nums, int k) {
        int sum1 = 0;
        int count = 0;
        HashMap<Integer, Integer> dp = new HashMap<>();
        dp.put(0,1);
        for (int i = 0; i < nums.length; i++) {
            sum1 += nums[i];
            int diff = sum1 - k;
            if (dp.containsKey(diff)) {
                count += dp.get(diff);
            }
            dp.putIfAbsent(sum1, 0);
            dp.put(sum1, dp.get(sum1)+1);
        }
        return count;
    }
}