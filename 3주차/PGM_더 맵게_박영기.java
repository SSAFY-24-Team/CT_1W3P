import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Long> pq = new PriorityQueue<>();
        for(int s : scoville){
            pq.add((long)s);
        }
        
        boolean flag = false;
        int answer = 0;
        while(true){
            if(pq.peek() >= K){
                flag = true;
                break;
            }
            
            if(pq.size() == 1){
                break;
            }
            
            pq.add(pq.poll() + pq.poll()*2);
            answer++;
        }
        
        return flag ? answer : -1;
    }
}
