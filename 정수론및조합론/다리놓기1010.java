package 정수론및조합론;
import java.io.*;
import java.util.StringTokenizer;

public class 다리놓기1010 {
    static Integer[][] dp;
    static int[] nArr;
    static int[] kArr;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        nArr = new int[n];
        kArr = new int[n];
        dp = new Integer[31][31];

        for(int i = 0;i < 31;i++){
            dp[i][0] = 1;
            dp[i][i] = 1;
        }

        for(int i = 0;i < n;i++){
            StringTokenizer str = new StringTokenizer(br.readLine());
            kArr[i] = Integer.parseInt(str.nextToken());
            nArr[i] = Integer.parseInt(str.nextToken());
        }

        for(int i = 0;i < n;i++){
            System.out.println(combination(nArr[i],kArr[i]));
        }
    }

    public static int combination(int n, int k){
        if(n == k || k == 0){
            return dp[n][k];
        }

        if(dp[n][k] == null){
            dp[n][k] = combination(n-1,k) + combination(n-1,k-1);
        }

        return dp[n][k];
    }
}
