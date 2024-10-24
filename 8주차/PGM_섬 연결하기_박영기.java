import java.util.*;

class Solution {
    public int solution(int n, int[][] costs) {
        ArrayList<Node>[] adjList = new ArrayList[n];
        for(int i=0; i<n; i++){
            adjList[i] = new ArrayList<>();
        }
        
        for(int[] c : costs){
            adjList[c[0]].add(new Node(c[1], c[2]));
            adjList[c[1]].add(new Node(c[0], c[2]));
        }
        
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(0, 0));
        
        int answer = 0;
        Node cur;
        boolean[] visited = new boolean[n];
        int cnt = 0;
        while(!pq.isEmpty()){
            cur = pq.poll();
            
            if(visited[cur.t])
                continue;
            
            visited[cur.t] = true;
            answer += cur.w;
            if(++cnt == n)
                return answer;
            
            for(Node next : adjList[cur.t]){
                if(visited[next.t])
                    continue;
                
                pq.add(new Node(next.t, next.w));
            }
        }
        
        return 0;
    }
    
    static class Node implements Comparable<Node>{
        int t, w;
        
        Node(int t, int w){
            this.t = t;
            this.w = w;
        }
        
        @Override
        public int compareTo(Node o1){
            return Integer.compare(this.w, o1.w);
        }
    }
}
