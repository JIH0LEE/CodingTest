package Greedy;
import java.io.*;
import java.util.StringTokenizer;

public class 잃어버린괄호1541 {
    static int[] sumPart;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        sumPart = new int[51];
        StringTokenizer str1 = new StringTokenizer(br.readLine(),"-");

        int length = 0;
        int index = 0;
        while(str1.hasMoreTokens()){
            StringTokenizer str2 = new StringTokenizer(str1.nextToken(),"+");
            while(str2.hasMoreTokens()){
                sumPart[index] += Integer.parseInt(str2.nextToken());
            }
            index++;
            length = index;
        }

        int answer = sumPart[0];
        for(int i = 1;i < length;i++){
            answer -= sumPart[i];
        }

        System.out.println(answer);
    }
}
