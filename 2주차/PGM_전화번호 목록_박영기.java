import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book, (s1, s2) -> {
            return s1.length() - s2.length();
        });
        
        Set<String> set = new HashSet<>();
        for(String str : phone_book){
            for(int i=1; i<=str.length(); i++){
                if(set.contains(str.substring(0, i)))
                    return false;
            }
            set.add(str);
        }
        
        return true;
    }
}
