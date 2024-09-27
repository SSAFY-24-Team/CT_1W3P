import java.util.*;

class Solution {
    static ArrayList<Integer>[] adjList;
    public int solution(int n, int[][] edge) {
        adjList = new ArrayList[n+1];
        for(int i=1; i<=n; i++){
            adjList[i] = new ArrayList<>();
        }
        
        for(int[] e : edge){
            adjList[e[0]].add(e[1]);
            adjList[e[1]].add(e[0]);
        }
        
        int answer = bfs(1, n);
        return answer;
    }
    
    static int bfs(int start, int n){
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(start);
        
        boolean[] visited = new boolean[n+1];
        visited[start] = true;
        
        int cur;
        int dist = 0;
        int size = 0;
        while(!queue.isEmpty()){
            size = queue.size();
            for(int i=0; i<size; i++){
                cur = queue.poll();
                for(int next : adjList[cur]){
                    if(visited[next])
                        continue;
                    queue.add(next);
                    visited[next] = true;
                }
            }
            dist++;
        }
        
        return size;
    } 
}
