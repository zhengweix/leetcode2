class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>((x, y) -> y - x);
        for (int i = 0; i < nums.length; i++)
            maxHeap.add(nums[i]);

        int result = 0;
        i = 0;
        while (i < k) {
            result = maxHeap.poll();
            i += 1;
        }

        return result;
    }

    public int findKthLargest1(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length - k];
    }
}