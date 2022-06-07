class Solution {
    public boolean isValid(String s) {
        ArrayList<Character> stack = new ArrayList();
        for (char c: s.toCharArray()){
            switch (c) {
                case '(':
                    stack.add(')');
                    break;
                case '[':
                    stack.add(']');
                    break;
                case '{':
                    stack.add('}');
                    break;
                default:
                    if (stack.size() == 0) {
                        return false;
                    }
                    if(c != stack.remove(stack.size() - 1)) {
                        return false;
                    }
            }
        }
        return stack == null;
    }
}