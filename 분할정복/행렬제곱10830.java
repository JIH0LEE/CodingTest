package 분할정복;
import java.io.*;
import java.util.StringTokenizer;

public class 행렬제곱10830 {
    static int matSize;
    static int[][] matrix;
    static long expo;
    static final int MOD = 1000;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str;
        StringBuilder sb = new StringBuilder();

        str = new StringTokenizer(br.readLine()," ");
        matSize = Integer.parseInt(str.nextToken());
        expo = Long.parseLong(str.nextToken());
        matrix = new int[matSize][matSize];

        for(int i = 0;i < matSize;i++){
            str = new StringTokenizer(br.readLine()," ");
            for(int j= 0;j < matSize;j++){
                matrix[i][j] = Integer.parseInt(str.nextToken());
            }
        }

        int[][] result = power(matrix,expo);

        for(int i = 0;i < matSize;i++){
            for(int j = 0;j <matSize;j++){
                sb.append(result[i][j]).append(" ");
            }
            sb.append('\n');
        }

        System.out.println(sb);
    }

    public static int[][] power(int[][] A,long B){
        for(int i = 0;i < matSize;i++){
            for(int j = 0;j < matSize;j++){
                A[i][j] %= MOD;
            }
        }
        if(B == 1){
            return A;
        }

        int[][] temp = power(A,B/2);

        if(B%2 == 1){
            return multiple(multiple(temp,temp),A);
        }

        return multiple(temp,temp);
    }

    public static int[][] multiple(int[][] first, int[][] second){
        int[][] result = new int[matSize][matSize];
        int sum = 0;
        for(int i = 0;i < matSize;i++){
            for(int j = 0;j < matSize;j++){
                for(int k = 0;k < matSize;k++){
                    sum += first[i][k]*second[k][j]%MOD;
                }
                result[i][j] = sum%MOD;
                sum = 0;
            }
        }
        return result;
    }
}
