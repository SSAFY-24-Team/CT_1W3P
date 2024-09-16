import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        TreeMap<Integer, Integer> map = new TreeMap<>();
        StringTokenizer st;
        int num, key;
        String op;
        for(String str : operations){
            st = new StringTokenizer(str);
            op = st.nextToken();
            num = Integer.parseInt(st.nextToken());
            
            if(op.equals("I")){
                map.put(num, map.getOrDefault(num, 0) + 1);    
            }else if(!map.isEmpty()){
                if(num == 1)
                    key = map.lastKey();
                else
                    key = map.firstKey();
                
                if(map.get(key) == 1)
                    map.remove(key);
                else
                    map.put(key, map.get(key) - 1);
            }
        }
                
        int[] answer = new int[2];
        answer[0] = map.isEmpty() ? 0 : map.lastKey();
        answer[1] = map.isEmpty() ? 0 : map.firstKey();
        return answer;
    }
}
