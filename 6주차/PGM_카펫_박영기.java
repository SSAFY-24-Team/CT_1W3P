class Solution {
    public int[] solution(int brown, int yellow) {
        int row, col;
        for(int i=2; i<=(brown-4)/2; i+=2){
            row = i / 2;
            col = (brown - 4 - i) / 2;
            if(row * col == yellow){
                return new int[]{col+2, row+2};
            }
        }
        return null;
    }
}
