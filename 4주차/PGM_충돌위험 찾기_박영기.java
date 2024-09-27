import java.util.*;

class Solution {
    static int[] dr = {-1,1,0,0};
    static int[] dc = {0,0,-1,1};
    static int R = 100;
    static int C = 100;
    public int solution(int[][] points, int[][] routes) {
        int n = points.length;
        int x = routes.length;
        int m = routes[0].length;
        
        ArrayList<Integer>[][] list = new ArrayList[n][n];
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(i == j)
                    continue;
                list[i][j] = new ArrayList<>();
                bfs(i, j, points, list);
            }
        }
    
        int[][] count = new int[(R+C)*m][R*C];
        int start, end, idx;
        for(int i=0; i<x; i++){
            idx = 0;
            for(int j=1; j<m; j++){
                start = routes[i][j-1]-1;
                end = routes[i][j]-1;
                for(int p : list[start][end]){
                    count[idx][p]++;
                    idx++;
                }
            }
            end = routes[i][m-1]-1;
            count[idx][(points[end][0]-1)*C + (points[end][1]-1)]++;
        }
        
        int answer = 0;
        for(int i=0; i<count.length; i++){
            for(int j=0; j<count[0].length; j++){
                if(count[i][j] > 1)
                    answer++;
            }
        }
        
        return answer;
    }
    
    static void bfs(int start, int end, int[][] points, ArrayList<Integer>[][] list){
        Point cur = new Point(points[start][0]-1, points[start][1]-1);
        
        Queue<Point> queue = new ArrayDeque<>();
        int[] visited = new int[R*C];
        
        queue.add(cur);
        visited[cur.r*C + cur.c] = -1;
        
        while(!queue.isEmpty()){
            cur = queue.poll();
            
            if(cur.r == points[end][0]-1 && cur.c == points[end][1]-1){
                Deque<Integer> stack = new ArrayDeque<>();
                int idx = cur.r*C + cur.c;
                idx = visited[idx];
                while(idx != -1){
                    stack.push(idx);
                    idx = visited[idx];
                }
                
                while(!stack.isEmpty()){
                    list[start][end].add(stack.pop());
                }
                
                return;
            }
            
            for(int i=0; i<4; i++){
                int nr = cur.r+dr[i];
                int nc = cur.c+dc[i];
                
                if(nr < 0 || nr >= R || nc < 0 || nc >= C || visited[nr*C + nc] != 0)
                    continue;
                
                queue.add(new Point(nr, nc));
                visited[nr*C + nc] = cur.r*C + cur.c;
            }
        }
    }
    
    static class Point{
        int r, c;
        
        Point(int r, int c){
            this.r = r;
            this.c = c;
        }
    }
}
