package Greedy;
import java.io.*;
import java.util.StringTokenizer;

public class 주유소13305 {
    static long[] length;
    static long[] price;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        length = new long[n-1];
        price = new long[n];

        StringTokenizer str1 = new StringTokenizer(br.readLine()," ");

        for(int i = 0;i < n-1;i++){
            length[i] = Integer.parseInt(str1.nextToken());
        }

        str1 = new StringTokenizer(br.readLine()," ");

        for(int i = 0;i < n;i++){
            price[i] = Integer.parseInt(str1.nextToken());
        }

        int index = 0;
        while(index != n-1){
            if(price[index] < price[index + 1]){
                price[index + 1] = price[index];
            }
            index++;
        }

        long sum = 0;
        for(int i = 0;i < n-1;i++){
            sum += price[i]*length[i];
        }

        System.out.println(sum);
    }
}
