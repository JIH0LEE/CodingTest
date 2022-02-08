package 분할정복;
import java.io.*;
import java.util.StringTokenizer;

public class 이항계수311401 {
    static int N;
    static int K;
    static final int MOD = 1000000007;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine()," ");
        N = Integer.parseInt(str.nextToken());
        K = Integer.parseInt(str.nextToken());

        System.out.println(factorial(N)*power(factorial(K)*factorial(N-K)%MOD,MOD-2)%MOD);
    }

    public static long factorial(int n){
        long result = 1;
        for(int i = 2;i <= n;i++){
            result *= i;
            result %= MOD;
        }

        return result%MOD;
    }

    public static long power(long base, long exp){
        if(exp == 1){
            return base%MOD;
        }

        long temp = power(base,exp/2);

        if(exp%2 == 1){
            return (base*temp%MOD)*temp%MOD;
        }

        return (temp%MOD)*(temp%MOD)%MOD;
    }
}
