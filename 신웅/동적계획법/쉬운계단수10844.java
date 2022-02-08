package 동적계획법;

import java.io.*;

public class 쉬운계단수10844 {
    static int n;
    static long [][] dp;
    static final long MOD = 1000000000;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        dp = new long[n+1][10];

        for(int i = 0;i < 10;i++){
            dp[1][i] = 1;
        }

        for(int i = 1;i < n;i++){
            for(int j = 0;j < 10;j++){
                if(j == 0){
                    dp[i+1][0] = dp[i][1];
                }else if(j == 9){
                    dp[i+1][9] = dp[i][8];
                }else{
                    dp[i+1][j] = (dp[i][j-1] + dp[i][j+1]) % MOD;
                }
            }
        }

        long sum = 0;
        for(int i = 1;i <= 9;i++){
            sum += dp[n][i] % MOD;
        }

        System.out.println(sum % MOD);
    }
}
