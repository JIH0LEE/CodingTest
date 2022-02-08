package 동적계획법;

import java.io.*;
import java.util.StringTokenizer;

public class 정수삼각형1932 {
    static Integer [][] triangle;
    static Integer [][] partialSum;
    static int N;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        triangle = new Integer[N][N];
        partialSum = new Integer[N][N];

        StringTokenizer str;

        for(int i = 0;i < N;i++){
            str = new StringTokenizer(br.readLine()," ");
            for(int j = 0;j < i + 1;j++){
                triangle[i][j] = Integer.parseInt(str.nextToken());
            }
        }

        for(int i = 0;i < N;i++){
            partialSum[N-1][i] = triangle[N-1][i];
        }

        System.out.println(optimalSum(0,0));
    }

    public static int optimalSum(int level, int index){
        if(level == N-1){
            return partialSum[level][index];
        }

        if(partialSum[level][index] == null){
            partialSum[level][index] =
                    Math.max(optimalSum(level + 1,index),optimalSum(level+1,index+1)) + triangle[level][index];
        }

        return partialSum[level][index];
    }
}
