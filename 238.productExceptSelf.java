class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len1 = nums.length;
        int[] res = new int[len1];
        ArrayList<Integer> zeros = new ArrayList<>();
        int prod = 1;
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (num == 0) {
                zeros.add(i);
            } else {
                prod = prod * num;
            }
        }
        int len2 = zeros.size();
        for (int j = 0; j < nums.length; j++) {
            if (len2 > 1) {
                res[j] = 0;
            } else if (len2 == 1) {
                if (j == zeros.get(0)) {
                    res[j] = prod;
                } else {
                    res[j] = 0;
                }
            } else {
                int prod1 = prod;
                res[j] = prod1/nums[j];
            }
        }
        return res;
    }

    public int[] productExceptSelf1(int[] nums) {
        int len1 = nums.length, left = 1, right = 1;
        int[] res = new int[len1];
        for (int i = 0; i < nums.length; i++) {
            res[i] = left;
            left *= nums[i];
        }
        for (int j = len1-1; j > -1; j--) {
            res[j] = res[j] * right;
            right *= nums[j];
        }
        return res;
    }
}