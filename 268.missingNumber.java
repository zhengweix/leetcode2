class Solution {
    public int missingNumber(int[] nums) {
        int i = 0, n = nums.length;
        while (i < n){
            int j = nums[i];
            if (j < n && nums[i] != nums[j]) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            } else {
                i++;
            }
        }
        for (i = 0; i < n; i++) {
            if (i != nums[i]) {
                return i;
            }
        }
        return n;
    }

    public int missingNumber1(int[] nums) {
        int x1 = 0;
        int n = nums.length;
        for (int i = 1; i <= n; i++)
            x1 ^= i;
        int x2 = nums[0];
        for (int j = 1; j < n; j++)
            x2 ^= nums[j];
        return x1^x2;
    }
}
