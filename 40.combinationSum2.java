class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        Set<List<Integer>>[] dp = new Set[target + 1];
        for (int i = 0; i <= target; i++) {
            dp[i] = new HashSet<>();
        }
        dp[0].add(new ArrayList<>());
        for (int cand: candidates) {
            if (cand > target) {
                break;
            }
            for (int i = target; i > cand-1; i--){
                for (List<Integer> lst : dp[i-cand]) {
                    List<Integer> newLst = new ArrayList<>(lst);
                    newLst.add(cand);
                    dp[i].add(newLst);
                }
            }
        }
        return new ArrayList<>(dp[target]);
    }
}