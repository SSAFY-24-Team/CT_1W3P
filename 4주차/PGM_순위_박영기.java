import java.util.*;

class Solution {
    static ArrayList<Integer>[] upList;
    static ArrayList<Integer>[] downList;
    static boolean[] visited;
    static int cnt;
    public int solution(int n, int[][] results) {
        upList = new ArrayList[n+1];
        downList = new ArrayList[n+1];
        for(int i=1; i<=n; i++){
            upList[i] = new ArrayList<>();
            downList[i] = new ArrayList<>();
        }
        
        int win, lose;
        for(int[] r : results){            
            upList[r[1]].add(r[0]);
            downList[r[0]].add(r[1]);
        }
        
        int answer = 0;
        for(int i=1; i<=n; i++){
            visited = new boolean[n+1];
            cnt = 1;
            visited[i] = true;
            
            up(i);
            down(i);
                        
            if(cnt == n)
                answer++;
        }
        
        return answer;
    }
    
    static void up(int num){
        for(int next : upList[num]){
            if(visited[next])
                continue;
            cnt++;
            visited[next] = true;
            up(next);
        }
    }
    
    static void down(int num){
        for(int next : downList[num]){
            if(visited[next])
                continue;
            cnt++;
            visited[next] = true;
            down(next);
        }
    }
}
