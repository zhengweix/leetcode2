class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int len1 = nums.length;
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i < len1; i++) {
            int num = nums[i];
            if (i > 0 && num == nums[i-1])
                continue;
            int left = i + 1;
            int right = len1 - 1;
            while (left < right) {
                int sum1 = num + nums[left] + nums[right];
                if (sum1 > 0) {
                    right--;
                } else if (sum1 < 0) {
                    left++;
                } else {
                    res.add(Arrays.asList(num, nums[left], nums[right]));
                    left++;
                    while (nums[left] == nums[left - 1] && left < right){
                        left++;
                    }
                }
            }
        }
        return res;
    }
}