import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        Set<Integer> set = new HashSet<>();
        int[] arr = {
                Integer.parseInt("111000000", 2), Integer.parseInt("000111000", 2), Integer.parseInt("000000111", 2),
                Integer.parseInt("100100100", 2), Integer.parseInt("010010010", 2), Integer.parseInt("001001001", 2),
                Integer.parseInt("100010001", 2), Integer.parseInt("001010100", 2)
        };
        boolean flag;
        while (T-- > 0) {
            for (int i = 0; i < 3; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 3; j++) {
                    sb.append(st.nextToken());
                }
            }

            int num = 0;
            for (int i = 0; i < sb.length(); i++) {
                if (sb.charAt(i) == 'H')
                    num |= (1 << (sb.length() - 1 - i));
            }
            sb.setLength(0);

            Queue<Integer> queue = new ArrayDeque<>();
            queue.add(num);

            set.clear();
            set.add(num);

            flag = false;
            int cur, size;
            int cnt = 0;
            outer:
            while (!queue.isEmpty()) {
                size = queue.size();
                for (int i = 0; i < size; i++) {
                    cur = queue.poll();

                    if (cur == 0 || cur == 511) {
                        bw.write(cnt + "\n");
                        flag = true;
                        break outer;
                    }

                    for (int j = 0; j < 8; j++) {
                        int next = cur ^ arr[j];

                        if (set.contains(next))
                            continue;

                        queue.add(next);
                        set.add(next);
                    }
                }
                cnt++;
            }

            if (!flag)
                bw.write(-1 + "\n");

        }
        bw.close();

    }
}
