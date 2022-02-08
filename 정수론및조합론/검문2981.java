package 정수론및조합론;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class 검문2981 {
    static int N;
    static long[] numbArr;
    static long[] chaArr;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        numbArr = new long[N];

        for(int i = 0;i < N;i++){
            numbArr[i] = Integer.parseInt(br.readLine());
        }

        long gcdVal = Math.abs(numbArr[0] - numbArr[1]);
        for(int i = 2;i < N;i++){
            gcdVal = GCD(gcdVal, Math.abs(numbArr[i] - numbArr[i-1]));
        }

        Stack<Long> stack = new Stack<Long>();
        for(long i = 2;i <= Math.sqrt(gcdVal);i++){
            if(i == Math.sqrt(gcdVal)){
                stack.push(i);
            }else {
                if (gcdVal % i == 0) {
                    System.out.print(i + " ");
                    stack.push(i);
                }
            }
        }

        while(!stack.isEmpty()){
            System.out.print(gcdVal/stack.pop() + " ");
        }
        System.out.print(gcdVal);
    }

    public static long GCD(long a, long b){
        while(b != 0){
            long r = a%b;
            a = b;
            b = r;
        }
        return a;
    }
}
