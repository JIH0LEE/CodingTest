package 동적계획법;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class LCS9251 {
    static char [] str1;
    static char [] str2;
    static Integer [][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        str1 = br.readLine().toCharArray();
        str2 = br.readLine().toCharArray();

        dp = new Integer [str1.length][str2.length];

        System.out.println(solve(str1.length-1, str2.length-1));
    }

    public static int solve(int x, int y){
        if(x == -1 || y == -1){
            return 0;
        }

        if(dp[x][y] == null){
            dp[x][y] = 0;

            if(str1[x] == str2[y]){
                dp[x][y] = solve(x-1,y-1) + 1;
            }else{
                dp[x][y] = Math.max(solve(x-1,y),solve(x,y-1));
            }
        }

        return dp[x][y];
    }
}
