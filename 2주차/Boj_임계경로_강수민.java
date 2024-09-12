import java.io.*;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Boj_임계경로_강수민 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int[] indegree = new int[n + 1];

        ArrayList<ArrayList<Edge>> adjList = new ArrayList<>();
        ArrayList<ArrayList<Edge>> adjList_reverse = new ArrayList<>();

        for (int i = 0; i <= n; i++) {
            adjList.add(new ArrayList<>());
            adjList_reverse.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int out = Integer.parseInt(st.nextToken());
            int in = Integer.parseInt(st.nextToken());
            int time = Integer.parseInt(st.nextToken());
            adjList.get(out).add(new Edge(in, time));
            adjList_reverse.get(in).add(new Edge(out, time));
            indegree[in]++;
        }

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());


        // 위상 정렬
        int[] critical_path = new int[n + 1]; // 걸린 시간의 최댓값
        Queue<Integer> que = new ArrayDeque<>();
        que.offer(start);

        while (!que.isEmpty()) {
            int now = que.poll();

            for (Edge next : adjList.get(now)) {
                critical_path[next.v] = Math.max(critical_path[next.v], critical_path[now] + next.time);
                if (--indegree[next.v] == 0) {
                    que.offer(next.v);
                }
            }
        }

        // 역방향 위상 정렬
        boolean[] visited = new boolean[n + 1];
        que.offer(end);
        int cnt = 0;

        while (!que.isEmpty()) {
            int now = que.poll();
            for (Edge next : adjList_reverse.get(now)) {
                if (critical_path[now] == critical_path[next.v] + next.time) {
                    cnt++;
                    if (!visited[next.v]) {
                        que.offer(next.v);
                        visited[next.v] = true;
                    }
                }
            }
        }

        sb.append(critical_path[end]).append('\n').append(cnt);
        bw.write(sb.toString());
        bw.flush();
    }

    private static class Edge {
        int v;
        int time;

        public Edge(int v, int time) {
            this.v = v;
            this.time = time;
        }
    }
}