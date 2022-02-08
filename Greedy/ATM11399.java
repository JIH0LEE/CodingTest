package Greedy;
import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class ATM11399 {
    static int n;
    static int[] numbArr;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        numbArr = new int[n];

        StringTokenizer str = new StringTokenizer(br.readLine()," ");

        for(int i = 0;i < n;i++){
            numbArr[i] = Integer.parseInt(str.nextToken());
        }

        Arrays.sort(numbArr);

        int answer = 0;

        for(int i = 0;i < n;i++){
            answer += numbArr[i] * (n-i);
        }

        System.out.println(answer);
    }
}
