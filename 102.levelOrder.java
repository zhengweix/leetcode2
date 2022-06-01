/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        if (root == null)
            return result;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int n = queue.size();
            int i = 0;
            List<Integer> result = new ArrayList<>();
            while (i < n) {
                TreeNode u = queue.poll();
                result.add(u.val);
                if (u.left != null)
                    queue.offer(u.left);
                if (u.right != null)
                    queue.offer(u.right);
                i++;
            }
            results.add(result);
        }
        return results;
    }
}
