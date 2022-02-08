package 정수론및조합론;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 조합0의개수2004 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine()," ");

        long N = Long.parseLong(str.nextToken());
        long K = Long.parseLong(str.nextToken());

        System.out.println(Math.min(countFive(N)-countFive(N-K)-countFive(K),countTwo(N)-countTwo(N-K)-countTwo(K)));
    }
    public static long countFive(long n){
        long count = 0;
        long divisor = 5;
        while(n/divisor != 0){
            count += n/divisor;
            divisor *= 5;
        }
        return count;
    }

    public static long countTwo(long n){
        long count = 0;
        long divisor = 2;
        while(n/divisor != 0){
            count += n/divisor;
            divisor *= 2;
        }
        return count;
    }
}
