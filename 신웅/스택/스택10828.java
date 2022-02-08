package 스택;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 스택10828 {
    static int N;
    static int top;
    static int stackSize;
    static int[] stackArr;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str1;
        N = Integer.parseInt(br.readLine());

        stackArr = new int[N];
        top = 0;
        stackSize = 0;

        for(int i = 0;i < N;i++){
            str1 = new StringTokenizer(br.readLine()," ");
            String str2 = str1.nextToken();
            if(str2.equals("pop")){
                pop();
            }
            if(str2.equals("size")){
                size();
            }
            if(str2.equals("empty")){
                empty();
            }
            if(str2.equals("top")){
                top();
            }
            if(str2.equals("push")){
                int m = Integer.parseInt(str1.nextToken());
                push(m);
            }
        }

        System.out.println(sb);
    }

    public static void push(int x){
        stackArr[top] = x;
        top++;
        stackSize++;
    }

    public static void pop(){
        if(stackSize == 0){
            sb.append(-1 + "\n");
        }else{
            sb.append(stackArr[top-1] + "\n");
            stackSize--;
            stackArr[top-1] = 0;
            top--;
        }
    }

    public static void size(){
        sb.append(stackSize + "\n");
    }

    public static void empty(){
        if(stackSize == 0){
            sb.append(1 + "\n");
        }else{
            sb.append(0+"\n");
        }
    }

    public static void top(){
        if(stackSize == 0){
            sb.append(-1 + "\n");
        }else{
            sb.append(stackArr[top-1] + "\n");
        }
    }
}
