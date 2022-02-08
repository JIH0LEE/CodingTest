package 동적계획법;

import java.io.*;
import java.util.StringTokenizer;

public class 연속합1912 {
    public static int n;
    static int [] numbArr;
    static Integer [] dp;
    static int max;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        numbArr = new int [n+1];
        dp = new Integer [n+1];
        StringTokenizer str = new StringTokenizer(br.readLine()," ");

        numbArr[0] = 0;
        dp[0] = 0;

        for(int i = 1;i <= n;i++){
            numbArr[i] = Integer.parseInt(str.nextToken());
        }

        dp[1] = numbArr[1];
        optimalSum(n);

        max = numbArr[1];
        for(int i = 1;i <= n;i++){
            if(max < dp[i]){
                max = dp[i];
            }
        }

        System.out.println(max);
    }

    public static int optimalSum(int N){
        if(dp[N] == null){
            dp[N] = Math.max(optimalSum(N-1) + numbArr[N], numbArr[N]);
        }

        return dp[N];
    }
}
