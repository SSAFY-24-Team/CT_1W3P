class Solution {
    static char[] arr = {'A', 'E', 'I', 'O', 'U'};
    static String sWord;
    static int answer = 0;
    static boolean flag = false;
    public int solution(String word) {
        sWord = word;
        dfs(0, "");
        return answer;
    }
    
    static void dfs(int idx, String str){        
        if(str.equals(sWord)){
            flag = true;
            return;
        }
        
        if(idx == 5){
            return;
        }
        
        for(char ch : arr){
            answer++;
            dfs(idx+1, str + ch);
            if(flag) return;
        }
    }
}
