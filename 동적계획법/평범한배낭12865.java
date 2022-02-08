package 동적계획법;

import java.io.*;
import java.util.StringTokenizer;

public class 평범한배낭12865 {
    static int [] p;
    static int [] w;
    static int N;
    static int W;
    static int [][] dp;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str1 = new StringTokenizer(br.readLine(), " ");

        N = Integer.parseInt(str1.nextToken());
        W = Integer.parseInt(str1.nextToken());

        p = new int[N+1];
        w = new int[N+1];
        p[0] = 0;
        w[0] = 0;

        dp = new int[N+1][W+1];

        for(int i = 1;i <= N;i++){
            StringTokenizer str2 = new StringTokenizer(br.readLine()," ");
            w[i] = Integer.parseInt(str2.nextToken());
            p[i] = Integer.parseInt(str2.nextToken());
        }

        for(int i = 1;i <= N;i++){
            for(int j = 1;j <= W;j++){
                if (w[i] > j) {
                    dp[i][j] = dp[i - 1][j];
                }
                if (w[i] <= j) {
                    dp[i][j] = Math.max(dp[i - 1][j],dp[i - 1][j - w[i]] + p[i]);
                }
            }
        }

        System.out.println(dp[N][W]);
    }
}
