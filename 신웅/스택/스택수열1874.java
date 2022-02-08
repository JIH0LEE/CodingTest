package 스택;
import java.io.*;
import java.util.Stack;
import java.util.*;

public class 스택수열1874 {
    static int n;
    static int[] numbArr;
    static int[] arr;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Integer> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        numbArr = new int[n];
        arr = new int[n];

        for(int i = 0;i < n;i++){
            numbArr[i] = Integer.parseInt(br.readLine());
            arr[i] = i+1;
        }

        int index1 = 0;
        int index2 = 0;
        while(true){
            if(!stack.empty() && stack.peek() == numbArr[index1]){
                stack.pop();
                sb.append("-").append("\n");
                index1++;
            }else{
                if(index2 != n){
                    stack.push(arr[index2]);
                    index2++;
                    sb.append("+").append("\n");
                }else{
                    sb.setLength(0);
                    sb.append("NO").append("\n");
                    break;
                }
            }

            if(index1 == n && index2 == n){
                break;
            }
        }

        System.out.println(sb);
    }
}