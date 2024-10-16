import java.util.*;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        Arrays.sort(rocks);
        
        int start = 1;
        int end = distance + 1;
        int mid, remove, next;
        while(start < end){
            mid = (start + end) / 2;
            remove = 0;
            
            next = mid;
            for(int rock : rocks){
                if(rock < next)
                    remove++;
                else
                    next = rock + mid;
            }
            if(distance < next)
                remove++;
            
            if(remove <= n)
                start = mid+1;
            else
                end = mid;
        }
        
        return end - 1;
    }
}
