import java.util.*;

class Solution {
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int len = 103;
        int[][] map = new int[len][len];
        int r1, r2, c1, c2;
        for(int[] rec : rectangle){
            c1 = rec[0] * 2;
            r1 = rec[1] * 2;
            c2 = rec[2] * 2;
            r2 = rec[3] * 2;
            for(int i=r1; i<=r2; i++){
                for(int j=c1; j<=c2; j++){
                    if(map[i][j] == 1)
                        continue;
                    
                    if(i == r1 || i == r2 || j == c1 || j == c2)
                        map[i][j] = 2;
                    else
                        map[i][j] = 1;
                }
            }
        }
        
        characterX *= 2;
        characterY *= 2;
        itemX *= 2;
        itemY *= 2;

        Queue<Point> queue = new ArrayDeque<>();
        queue.add(new Point(characterY, characterX));
        boolean[][] visited = new boolean[len][len];
        visited[characterY][characterX] = true;
        
        int[] dr = {-1,1,0,0};
        int[] dc = {0,0,-1,1};
        Point cur;
        int size;
        int dist = 0;
        while(!queue.isEmpty()){
            size = queue.size();
            
            for(int i=0; i<size; i++){
                cur = queue.poll();
                
                if(cur.r == itemY && cur.c == itemX){
                    return dist/2;
                }
                
                for(int j=0; j<4; j++){
                    int nr = cur.r+dr[j];
                    int nc = cur.c+dc[j];
                    
                    if(map[nr][nc] != 2 || visited[nr][nc])
                        continue;
                    
                    queue.add(new Point(nr, nc));
                    visited[nr][nc] = true;
                }
            }
            
            dist++;
        }
            
        return 0;
    }
    
    static class Point{
        int r, c;
        
        Point(int r, int c){
            this.r = r;
            this.c = c;
        }
    }
}
