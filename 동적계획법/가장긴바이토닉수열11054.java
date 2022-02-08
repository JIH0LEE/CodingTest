package 동적계획법;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 가장긴바이토닉수열11054 {
    static int[][] dp;
    static int n;
    static int[] setArr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        setArr = new int[n+1];
        StringTokenizer str = new StringTokenizer(br.readLine()," ");

        for(int i = 1;i <= n;i++){
            setArr[i] = Integer.parseInt(str.nextToken());
        }

        dp = new int[n+1][2];     //0일때 중간에 내려가는 수열, 1일때 계속올라가는 수열

        for(int i = 1;i <= n;i++){
            for(int j = 0;j < 2;j++){
                dp[i][j] = 1;
            }
        }


        for(int i = 1;i <= n;i++){
            for(int j = 1;j < i;j++){
                if((setArr[i] > setArr[j])&&(dp[i][1] <= dp[j][1])){
                    dp[i][1] = dp[j][1] + 1;
                }
                if((setArr[i] < setArr[j])&&(dp[i][0] <= Math.max(dp[j][1],dp[j][0]))){
                    dp[i][0] = Math.max(dp[j][1],dp[j][0]) + 1;
                }
            }
        }

        int max = 0;
        for(int i = 1;i <= n;i++){
            if(max < Math.max(dp[i][0],dp[i][1])){
                max = Math.max(dp[i][0],dp[i][1]);
            }
        }

        System.out.println(max);
    }
}
