package 동적계획법;

import java.io.*;
import java.util.StringTokenizer;

public class 가장긴증가하는부분수열11053 {
    static int n;
    static int [] numbArr;
    static Integer [] dp;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        numbArr = new int[n+1];
        dp = new Integer[n+1];

        numbArr[0] = 0;
        dp[0] = 0;
        StringTokenizer str = new StringTokenizer(br.readLine()," ");
        for(int i = 1;i <= n;i++){
            numbArr[i] = Integer.parseInt(str.nextToken());
            dp[i] = 1;
        }

        for(int i = 1;i <= n;i++){
            for(int j = 1;j < i;j++){
                if((numbArr[i] > numbArr[j])&&(dp[i] <= dp[j])){
                    dp[i] = dp[j] + 1;
                }
            }
        }

        int max = 0;
        for(int i = 1;i <= n;i++){
            if(max < dp[i]){
                max = dp[i];
            }
        }

        System.out.println(max);
    }
}
