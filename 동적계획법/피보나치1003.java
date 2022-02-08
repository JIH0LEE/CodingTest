package 동적계획법;

import java.io.*;

public class 피보나치1003 {
    static StringBuilder sb = new StringBuilder();
    static Integer [][] cntArr = new Integer[41][2];
    static int test;
    static int testNum;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        testNum = Integer.parseInt(br.readLine());

        cntArr[0][0] = 1;
        cntArr[0][1] = 0;
        cntArr[1][0] = 0;
        cntArr[1][1] = 1;

        for(int i = 0;i < testNum;i++){
            test = Integer.parseInt(br.readLine());
            sb.append(fibonacci(test)[0]).append(" ").append(fibonacci(test)[1]).append("\n");
        }

        System.out.println(sb);
    }

    static Integer [] fibonacci(int n){
        if((cntArr[n][0] == null) || (cntArr[n][1] == null)){
            cntArr[n][0] = fibonacci(n-1)[0] + fibonacci(n-2)[0];
            cntArr[n][1] = fibonacci(n-1)[1] + fibonacci(n-2)[1];
        }
        return cntArr[n];
    }
}
