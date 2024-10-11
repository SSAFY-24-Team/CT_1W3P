class Solution {
    static boolean[] visited;
    static int[][] arr;
    static int answer = -1;
    public int solution(int k, int[][] dungeons) {
        arr = dungeons;
        visited = new boolean[arr.length];
        dfs(0, k);
        return answer;
    }
    
    static void dfs(int cnt, int score){        
        answer = Math.max(answer, cnt);
        for(int i=0; i<arr.length; i++){
            if(visited[i] || arr[i][0] > score)
                continue;
            
            visited[i] = true;
            dfs(cnt+1, score-arr[i][1]);
            visited[i] = false;
        }
    }
}
