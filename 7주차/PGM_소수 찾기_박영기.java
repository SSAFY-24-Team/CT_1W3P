import java.util.*;

class Solution {
    static char[] arr;
    static boolean[] visited, isNotPrime;
    static Set<Integer> set;
    public int solution(String numbers) {
        set = new HashSet<>();
        arr = numbers.toCharArray();
        visited = new boolean[arr.length];
        
        int len = (int)Math.pow(10, 7);
        isNotPrime = new boolean[len];
        isNotPrime[0] = isNotPrime[1] = true;
        for(int i=2; i<=Math.sqrt(len); i++){
            if(isNotPrime[i])
                continue;
            for(int j=i*i; j<len; j+=i){
                isNotPrime[j] = true;
            }
        }
        
        perm(0, 0);
        return set.size();
    }
    
    static void perm(int idx, int num){
        if(!isNotPrime[num])
            set.add(num);   
        
        for(int i=0; i<arr.length; i++){
            if(visited[i])
                continue;
            visited[i] = true;
            perm(idx+1, num * 10 + Character.getNumericValue(arr[i]));
            visited[i] = false;
        }
    }
}
