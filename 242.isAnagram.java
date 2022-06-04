class Solution {
    public boolean isAnagram(String s, String t) {
        int[] letters = new int[26];
        for (char c: s.toCharArray()) {
            letters[c-'a']++;
        }
        for (char c: t.toCharArray()) {
            letters[c-'a']--;
        }
        for(int i : letters) {
            if(l != 0)
                return false;
        }
        return true;
    }

    public boolean isAnagram1(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        HashMap<Character, Integer> chars1 = new HashMap<>();
        for (char c: s.toCharArray()) {
            chars1.put(c, chars1.getOrDefault(c, 0)+1);
        }
        HashMap<Character, Integer> chars2 = new HashMap<>();
        for (char c: t.toCharArray()) {
            chars2.put(c, chars2.getOrDefault(c, 0)+1);
        }
        for(Character c : chars1.keySet()){
            int val1 = chars1.get(c);
            int val2 = chars2.getOrDefault(c , 0);
            if(val1 != val2){
                return false;
            }
        }
        return true;
    }
}