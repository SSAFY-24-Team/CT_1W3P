import java.util.*;

class Solution {
    public String solution(String number, int k) {
        Deque<Character> stack = new ArrayDeque<>();
        for(char ch : number.toCharArray()){
            while(!stack.isEmpty() && stack.peek() < ch && k > 0){
                stack.pop();
                k--;
            }
            stack.push(ch);
        }
        
        while(k > 0){
            stack.pop();
            k--;
        }
        
        StringBuilder sb = new StringBuilder();
        while(!stack.isEmpty()){
            sb.append(stack.pop());
        }
        
        String answer = sb.reverse().toString();
        return answer;
    }
}
