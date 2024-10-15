class Solution {
    public int solution(int n) {

        int a = 1;
        int b = 1;

        for(int i = 2; i <= n; i++) {
            int temp = b;
            b = (a + b) % 1_000_000_007;
            a = temp;
        }

        return b;
    }
}

/*
n   dp[n]
1   1
2   2
3   3
4   5
5   8

*/