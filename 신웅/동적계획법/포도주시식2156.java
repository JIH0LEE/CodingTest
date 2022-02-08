package 동적계획법;

import java.io.*;

public class 포도주시식2156 {
    static int [] podoju;
    static Integer [] optimalSum;
    static int n;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        podoju = new int [n+1];
        optimalSum = new Integer[n+1];

        for(int i = 1;i < n+1;i++){
            podoju[i] = Integer.parseInt(br.readLine());
        }

        optimalSum[0] = 0;
        optimalSum[1] = podoju[1];
        if(n > 1) {
            optimalSum[2] = podoju[1] + podoju[2];
        }

        System.out.println(solve(n));
    }

    public static int solve(int N){
        if(optimalSum[N] == null){
            optimalSum[N] = Math.max(Math.max(solve(N-2),solve(N-3) + podoju[N-1]) + podoju[N], solve(N-1));
        }

        return optimalSum[N];
    }
}
