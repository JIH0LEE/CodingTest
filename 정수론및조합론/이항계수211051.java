package 정수론및조합론;
import java.io.*;
import java.util.StringTokenizer;

public class 이항계수211051 {
    static int N;
    static int K;
    static Integer[][] dp;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine()," ");

        N = Integer.parseInt(str.nextToken());
        K = Integer.parseInt(str.nextToken());

        dp = new Integer[N+1][N+1];

        for(int i = 0;i <= N;i++){
            dp[i][0] = 1;
            dp[i][i] = 1;
        }

        System.out.println(combination(N,K)%10007);
    }

    public static int combination(int n, int k){
        if(n == k || k == 0){
            return dp[n][k];
        }

        if(dp[n][k] == null){
            dp[n][k] = combination(n-1,k)%10007 + combination(n-1,k-1)%10007;
        }

        return dp[n][k]%10007;
    }
}
