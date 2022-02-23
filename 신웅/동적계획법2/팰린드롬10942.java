package 동적계획법2;

import java.io.*;
import java.util.StringTokenizer;

public class 팰린드롬10942 {
    static int N;
    static int M;
    static boolean dp[][];
    static String num[];
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        dp = new boolean[N+1][N+1];
        num = new String[N+1];

        for(int i=1;i<=N;i++){
            num[i] = st.nextToken();
        }

        Palindrome();
        M = Integer.parseInt(br.readLine());

        for(int i=0;i<M;i++){
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());

            if(dp[from][to]){
                bw.write("1");
            }
            else{
                bw.write("0");
            }
            bw.newLine();
        }
        bw.close();
    }
    static public void Palindrome(){
        for(int i=1;i<=N;i++){
            dp[i][i] = true;
        }
        for(int i=2;i<=N;i++){
            if(num[i-1].equals(num[i])){
                dp[i-1][i] = true;
            }
            else{
                dp[i-1][i] = false;
            }
        }

        for(int i=2;i<=N-1;i++){
            for(int j=1;j+i<=N;j++){
                if(num[j].equals(num[j+i]) && dp[j+1][j+i-1]){
                    dp[j][j+i] = true;
                }
            }
        }
    }
}