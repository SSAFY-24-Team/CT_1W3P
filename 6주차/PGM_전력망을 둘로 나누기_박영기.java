import java.util.*;

class Solution {
    static ArrayList<Integer>[] adjList;
    public int solution(int n, int[][] wires) {
        adjList = new ArrayList[n+1];
        for(int i=1; i<=n; i++){
            adjList[i] = new ArrayList<>();
        }
        
        for(int[] w : wires){
            adjList[w[0]].add(w[1]);
            adjList[w[1]].add(w[0]);
        }
        
        int abs;
        int answer = Integer.MAX_VALUE;
        boolean[] visited;
        for(int[] w : wires){
            abs = -1;
            visited = new boolean[n+1];
            for(int i=1; i<=n; i++){
                if(visited[i])
                    continue;
                
                if(abs == -1)
                    abs = bfs(i, w, visited);    
                else 
                    abs = Math.abs(abs - bfs(i, w, visited));
                
            }
            
            answer = Math.min(answer, abs);
        }
        
        return answer;
    }
    
    static int bfs(int start, int[] remove, boolean[] visited){
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(start);
        visited[start] = true;
        
        int cur;
        int cnt = 0;
        while(!queue.isEmpty()){
            cur = queue.poll();
            cnt++;
            
            for(int next : adjList[cur]){
                if(visited[next] || 
                   cur == remove[0] && next == remove[1] ||
                  cur == remove[1] && next == remove[0])
                    continue;
                
                queue.add(next);
                visited[next] = true;
            }
        }
        
        return cnt;
    }
}
