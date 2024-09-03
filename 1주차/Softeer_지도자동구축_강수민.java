import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        bw.write(Integer.toString(dfs(Integer.parseInt(br.readLine()))));
        bw.flush();
    }

    private static int dfs(int n) {
        if (n == 0) {
            return 4;
        }

        return dfs(n - 1) * 4 - ((int)Math.pow(2, n-1) * 4) - 3;
    }
}