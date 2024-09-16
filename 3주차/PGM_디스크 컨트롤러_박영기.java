import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        PriorityQueue<Work> pq1 = new PriorityQueue<>((w1, w2) -> {
            if(w1.request == w2.request){
                return w1.spend - w2.spend;
            }
            return w1.request - w2.request;
        });
        
        PriorityQueue<Work> pq2 = new PriorityQueue<>((w1, w2) -> {
            if(w1.spend == w2.spend){
                return w1.request - w2.request;
            }
            return w1.spend - w2.spend;
        });
        
        for(int[] j : jobs){
            pq1.add(new Work(j[0], j[1]));
        }
        
        Work cur;
        int time = 0;
        int answer = 0;
        while(!pq1.isEmpty()){
            while(!pq1.isEmpty() && pq1.peek().request < time){
                pq2.add(pq1.poll());
            }
            
            if(pq2.isEmpty()){
                cur = pq1.poll();
                time = cur.request + cur.spend;
            }else{
                cur = pq2.poll();
                while(!pq2.isEmpty()){
                    pq1.add(pq2.poll());
                }
                time += cur.spend;
            }
            
            answer += time - cur.request;
        }
        
        return answer / jobs.length;
    }
    
    static class Work{
        int request, spend;
        
        Work(int request, int spend){
            this.request = request;
            this.spend = spend;
        }
    }
}
