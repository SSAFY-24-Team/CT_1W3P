import java.util.*;

class Solution {
    public int solution(int[][] routes) {
        Arrays.sort(routes, (o1, o2) -> {
            if(o1[1] == o2[1]) return Integer.compare(o1[0], o2[0]);
            return Integer.compare(o1[1], o2[1]);
        });
        
        int answer = 0;
        int camera = Integer.MIN_VALUE;
        for(int[] arr : routes){
            if(camera < arr[0]){
                answer++;
                camera = arr[1];
            }
        }
        
        return answer;
    }
}
