package 백트래킹;

import java.io.*;
import java.util.StringTokenizer;

public class N과M1 {
    static boolean check [];
    static int result [];
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer str = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(str.nextToken());
        int M = Integer.parseInt(str.nextToken());

        result = new int[N];
        check = new boolean[N];

        dfs(N,M,0);
    }

    public static void dfs(int N, int M, int level){
        if(level == M){
            for(int i = 0;i < M;i++){
                System.out.print(result[i] + " ");
            }
            System.out.println();
        }

        for(int i = 0;i < N;i++){
            if(!check[i]){
                check[i] = true;
                result[level] = i + 1;
                dfs(N,M,level + 1);
                check[i] = false;
            }
        }
    }
}
