package 동적계획법2;

import java.io.*;
import java.util.StringTokenizer;

public class 행렬곱셈순서11049 {
    static int N;
    static int[][] dp;
    static int[][] matrix;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        dp = new int[N][N];
        matrix = new int[N][2];
        StringTokenizer str;
        for(int i = 0;i < N;i++){
            str = new StringTokenizer(br.readLine()," ");
            matrix[i][0] = Integer.parseInt(str.nextToken());
            matrix[i][1] = Integer.parseInt(str.nextToken());
        }
        for(int i = 0;i < N;i++){
            for(int j = 0;j < N;j++){
                if(i == j){
                    dp[i][j] = 0;
                }else{
                    dp[i][j] = Integer.MAX_VALUE;
                }
            }
        }
        System.out.println(find(0,N-1));
    }

    public static int find(int start, int end){
        if(start == end){
            return 0;
        }
        if(dp[start][end] != Integer.MAX_VALUE){
            return dp[start][end];
        }

        for(int i = start;i < end;i++){
            int temp = find(start,i) + find(i+1,end) + matrix[start][0]*matrix[i][1]*matrix[end][1];
            dp[start][end] = Math.min(dp[start][end], temp);
        }

        return dp[start][end];
    }
}
