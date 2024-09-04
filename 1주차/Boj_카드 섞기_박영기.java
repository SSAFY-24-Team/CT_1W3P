import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int K;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] cards = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }

        K = 1;
        while (Math.pow(2, K) < N) {
            K++;
        }
        K--;

        int[] arr = new int[N];
        for (int i = 1; i <= K; i++) {
            for (int j = 1; j <= K; j++) {

                for (int k = 0; k < N; k++) {
                    arr[k] = k + 1;
                }

                recover(j, arr);
                recover(i, arr);

                boolean flag = true;
                for (int k = 0; k < N; k++) {
                    if (arr[k] != cards[k]) {
                        flag = false;
                        break;
                    }
                }

                if (flag) {
                    System.out.println(j + " " + i);
                    return;
                }
            }
        }
    }

    static void recover(int k, int[] arr) {
        int stage = 1;
        int len;

        int[] sub1, sub2;
        int last = arr.length;
        while (stage <= k + 1) {
            len = (int) Math.pow(2, k - stage + 1);
            sub2 = new int[len];
            sub1 = new int[last - sub2.length];

            for (int i = 0; i < last; i++) {
                if (i < last - len) {
                    sub1[i] = arr[i];
                } else {
                    sub2[i- sub1.length] = arr[i];
                }
            }

            for (int i = 0; i < last; i++) {
                if (i < sub2.length) {
                    arr[i] = sub2[i];
                } else {
                    arr[i] = sub1[i - sub2.length];
                }
            }

            last = sub2.length;
            stage++;
        }
    }
}
