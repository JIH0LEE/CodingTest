package 스택;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Stack;

public class 균형잡힌세상4949 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        Stack<Character> stack = new Stack<>();

        while(true){
            String str = br.readLine();
            if(str.equals(".")){
                break;
            }

            char c;
            for(int i = 0;i < str.length();i++){
                c = str.charAt(i);
                if(c == '('){
                    stack.push('(');
                }
                else if(c == '['){
                    stack.push('[');
                }
                else if(c == ')'){
                    if(!stack.isEmpty()) {
                        if (stack.peek() == '(') {
                            stack.pop();
                        } else {
                            stack.push('x');
                        }
                    }else{
                        stack.push('x');
                    }
                }
                else if(c == ']'){
                    if(!stack.isEmpty()) {
                        if (stack.peek() == '[') {
                            stack.pop();
                        } else {
                            stack.push('x');
                        }
                    }else{
                        stack.push('x');
                    }
                }
            }
            if(stack.isEmpty()){
                sb.append("yes").append("\n");
                stack.clear();
            }else{
                sb.append("no").append("\n");
                stack.clear();
            }

        }

        System.out.println(sb);
    }
}
