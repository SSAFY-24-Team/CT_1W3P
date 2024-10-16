class Solution {
    public long solution(int n, int[] times) {
        long start = Integer.MAX_VALUE;
        long end = Integer.MIN_VALUE;
        for(int time : times){
            start = Math.min(start, time);
            end = Math.max(end, time);
        }
        end *= n;
        
        long target = (long) n;
        long mid, cnt;
        while(start < end){
            mid = (start + end) / 2;
            cnt = 0;
            for(int time : times){
                cnt += mid / time;
            }
            
            if(cnt < target)
                start = mid + 1;
            else
                end = mid;
        }
        
        return end;
    }
}
