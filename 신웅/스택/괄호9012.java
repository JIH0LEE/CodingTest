package 스택;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class 괄호9012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        Stack<Boolean> stack = new Stack<>();
        String s;
        for(int i = 0;i < T;i++){
            s = br.readLine();
            for(int j = 0;j < s.length();j++){
                char c = s.charAt(j);
                if(c == '('){
                    stack.push(true);
                }
                if(stack.isEmpty()){
                    if(c == ')'){
                        stack.push(true);
                        break;
                    }
                }
                if(!stack.isEmpty()){
                    if(c == ')'){
                        stack.pop();
                    }
                }
            }
            if(stack.isEmpty()){
                sb.append("YES").append("\n");
                stack.clear();
            }else{
                sb.append("NO").append("\n");
                stack.clear();
            }
        }

        System.out.println(sb);
    }

}
