class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int start = 1;
        int end = (int)Math.pow(10, 5);
        int level;
        long total;
        while(start < end){
            level = (start + end) / 2;
            total = 0;
            for(int i=0; i<diffs.length; i++){
                if(diffs[i] <= level)
                    total += times[i];
                else
                    total += (times[i] + times[i-1]) * (diffs[i]-level) + times[i];
            }
            
            if(total > limit)
                start = level + 1;
            else
                end = level;
        }
        
        int answer = end;
        return answer;
    }
}
