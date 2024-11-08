import java.util.*;

class Solution {
    public int solution(int N, int number) {
        Set<Integer>[] set = new Set[9];
        for(int i=1; i<=8; i++){
            set[i] = new HashSet<>();
        }
        
        int n = 0;
        for(int i=1; i<=8; i++){
            n *= 10;
            n += N;
            set[i].add(n);
            
            for(int j=1; j<i; j++){
                for(int num1 : set[j]){
                    for(int num2 : set[i-j]){
                        set[i].add(num1 + num2);
                        set[i].add(num1 - num2);
                        set[i].add(num1 * num2);
                        if(num2 != 0)
                            set[i].add(num1 / num2);
                    }
                }
            }
            
            if(set[i].contains(number))
                return i;
        }
        
        return -1;
    }
}
