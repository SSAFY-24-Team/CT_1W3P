import java.util.*;

class Solution {
    public int solution(String arr[]) {
        int len = arr.length;
        int[][] max = new int[len][len];
        int[][] min = new int[len][len];
        for(int i=0; i<len; i++){
            Arrays.fill(max[i], Integer.MIN_VALUE);
            Arrays.fill(min[i], Integer.MAX_VALUE);
        }
        
        for(int i=0; i<len; i+=2){
            for(int j=0; j<len-i; j+=2){
                if(i == 0){
                    max[j][j] = Integer.parseInt(arr[j]);
                    min[j][j] = Integer.parseInt(arr[j]);
                }else{
                    for(int k=j+1; k<j+i; k+=2){
                        if(arr[k].equals("-")){
                            max[j][j+i] = Math.max(max[j][j+i], max[j][k-1] - min[k+1][j+i]);//최대 - 최소
                            min[j][j+i] = Math.min(min[j][j+i], min[j][k-1] - max[k+1][j+i]);//최소 - 최대
                        }else{
                            max[j][j+i] = Math.max(max[j][j+i], max[j][k-1] + max[k+1][j+i]);//최대 + 최대
                            min[j][j+i] = Math.min(min[j][j+i], min[j][k-1] + min[k+1][j+i]);//최소 + 최소
                        }
                    }   
                }
            }
        }
        
        int answer = max[0][len-1];
        return answer;
    }
}
