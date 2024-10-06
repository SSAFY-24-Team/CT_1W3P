import java.util.*;

class Solution {
    public int solution(int[][] game_board, int[][] table) {
        int len = table.length;
        int[] dr = {-1,1,0,0};
        int[] dc = {0,0,-1,1};
        
        //퍼즐찾기
        Queue<Point> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[len][len];
        List<List<Point>> pList = new ArrayList<>();
        for(int i=0; i<len; i++){
            for(int j=0; j<len; j++){
                if(visited[i][j] || table[i][j] != 1)
                    continue;
                
                pList.add(new ArrayList<>());
                queue.add(new Point(i, j));
                visited[i][j] = true;
                
                Point cur;
                while(!queue.isEmpty()){
                    cur = queue.poll();
                    pList.get(pList.size()-1).add(cur);
                    
                    for(int d=0; d<4; d++){
                        int nr = cur.r+dr[d];
                        int nc = cur.c+dc[d];
                        
                        if(nr < 0 || nr >= len || nc < 0 || nc >= len ||
                          visited[nr][nc] || table[nr][nc] != 1)
                            continue;
                        
                        queue.add(new Point(nr, nc));
                        visited[nr][nc] = true;
                    }
                }
            }    
        }
        
        int answer = 0;
        List<Point> temp;
        int[][] rotMap;
        for(int t=0; t<4; t++){
            //빈 공간 찾기
            visited = new boolean[len][len];
            for(int i=0; i<len; i++){
                for(int j=0; j<len; j++){
                    if(game_board[i][j] != 0 || visited[i][j])
                        continue;
                    
                    temp = new ArrayList<>();
                    queue.add(new Point(i, j));
                    visited[i][j] = true;
                    
                    Point cur;
                    while(!queue.isEmpty()){
                        cur = queue.poll();
                        temp.add(cur);
                        
                        for(int d=0; d<4; d++){
                            int nr = cur.r+dr[d];
                            int nc = cur.c+dc[d];
                            
                            if(nr < 0 || nr >= len || nc < 0 || nc >= len ||
                              visited[nr][nc] || game_board[nr][nc] != 0)
                                continue;
                            
                            queue.add(new Point(nr, nc));
                            visited[nr][nc] =  true;
                        }
                    }
                    
                    //퍼즐 끼우기
                    int tr, tc;
                    outer:
                    for(List<Point> puzzle : pList){
                        if(puzzle.size() != temp.size())
                            continue;
                        
                        tr = puzzle.get(0).r - temp.get(0).r;
                        tc = puzzle.get(0).c - temp.get(0).c;
                        for(int p=0; p<puzzle.size(); p++){
                            if(puzzle.get(p).r != temp.get(p).r + tr ||
                              puzzle.get(p).c != temp.get(p).c + tc)
                                continue outer;
                        }
                        
                        answer += puzzle.size();
                        puzzle.clear();
                        
                        for(Point p : temp){
                            game_board[p.r][p.c] = 1;
                        }
                        
                        break;
                    }
                }
            }
            
            //게임보드 회전
            rotMap = new int[len][len];
            for(int i=0; i<len; i++){
                for(int j=0; j<len; j++){
                    rotMap[j][len-1-i] = game_board[i][j];
                }
            }
            
            game_board = rotMap;
        }
        
        return answer;
    }
    
    static class Point {
        int r,c;
        
        Point(int r, int c){
            this.r = r;
            this.c = c;
        }
        
        @Override
        public String toString(){
            return "r: " + this.r + " / "+ "c: " + this.c;
        }
    }
}
