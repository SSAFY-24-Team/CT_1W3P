import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] arr = new int[N][M];
        String row;
        for (int i = 0; i < N; i++) {
            row = br.readLine();
            for (int j = 0; j < M; j++) {
                arr[i][j] = row.charAt(j) - '0';
            }
        }

        int ans = -1;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                for (int k = -N; k <= N; k++) {
                    for (int l = -M; l <= M; l++) {
                        int r = i;
                        int c = j;
                        int num = 0;
                        while (0 <= r && r < N && 0 <= c && c < M) {
                            num = num * 10 + arr[r][c];

                            int n = (int) Math.sqrt(num);
                            if (n * n == num) {
                                ans = Math.max(ans, num);
                            }

                            if (k == 0 && l == 0) break;
                            r += k;
                            c += l;
                        }
                    }
                }
            }
        }

        System.out.println(ans);
    }
}
