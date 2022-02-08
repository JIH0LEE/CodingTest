package 스택;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class 제로10773 {
    static int K;
    static int[] numbArr;
    static int sum;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        K = Integer.parseInt(br.readLine());
        numbArr = new int[K];

        Stack<Integer> stack = new Stack<>();
        for(int i = 0;i < K;i++){
            numbArr[i] = Integer.parseInt(br.readLine());
            if(numbArr[i] == 0){
                stack.pop();
            }else{
                stack.push(numbArr[i]);
            }
        }

        sum = 0;

        while(!stack.isEmpty()){
            sum += stack.peek();
            stack.pop();
        }

        System.out.println(sum);
    }
}
