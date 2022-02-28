package DFS와BFS;
import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 토마토7576 {
    static int M;
    static int N;
    static int[][] graph;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static Queue<tomato> queue = new LinkedList<>();
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine()," ");
        N = Integer.parseInt(str.nextToken());
        M = Integer.parseInt(str.nextToken());
        graph = new int[M][N];
        for(int i = 0;i < M;i++){
            str = new StringTokenizer(br.readLine());
            for(int j = 0;j < N;j++){
                graph[i][j] = Integer.parseInt(str.nextToken());
                if(graph[i][j] == 1){
                    queue.offer(new tomato(i,j));
                }
            }
        }
        bfs();
        int result = 0;
        loop :
        for(int i = 0;i < M;i++){
            for(int j = 0;j < N;j++){
                if(graph[i][j] == 0){
                    result = -1;
                    break loop;
                }else{
                    result = Math.max(result, graph[i][j]);
                }
            }
        }
        if(result == -1){
            System.out.println(result);
        }else{
            System.out.println(result - 1);
        }
    }

    public static void bfs(){
        while(!queue.isEmpty()){
            tomato node = queue.poll();
            for(int i = 0;i < 4;i++){
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];
                if(nx <= -1 || ny <= -1 || nx >= M || ny >= N){
                    continue;
                }else{
                    if(graph[nx][ny] == 0){
                        queue.offer(new tomato(nx,ny));
                        graph[nx][ny] = graph[node.x][node.y] + 1;
                    }
                }
            }
        }
    }

    public static class tomato{
        int x;
        int y;

        tomato(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
}

