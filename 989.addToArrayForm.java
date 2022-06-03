class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        ArrayList<Integer> numList = new ArrayList<>();
        for (int i = num.length - 1; i >= 0; i--) {
            int sum = num[i] + k;
            numList.add(sum%10);
            k = sum/10;
        }
        while (k > 0) {
            numList.add(k%10);
            k /= 10;
        }
        Collections.reverse(numList);
        return numList;
    }
}