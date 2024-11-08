class Solution {
    public int solution(int[] money) {
        int len = money.length;
        int[] dp = new int[len-1];
        int answer = 0;
        dp[0] = money[0];
        dp[1] = Math.max(money[1], dp[0]);
        for(int i=2; i<len-1; i++){
            dp[i] = Math.max(dp[i-2] + money[i], dp[i-1]);
        }
        answer = dp[len-2];
        
        dp[0] = money[1];
        dp[1] = Math.max(money[2], dp[0]);
        for(int i=3; i<len; i++){
            dp[i-1] = Math.max(dp[i-3] + money[i], dp[i-2]);
        }
        answer = Math.max(answer, dp[len-2]);
        
        return answer;
    }
}
