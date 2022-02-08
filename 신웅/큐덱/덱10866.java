package 큐덱;
import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class 덱10866 {
    static int n;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        Deque<Integer> deque = new ArrayDeque<>();
        StringTokenizer str;

        n = Integer.parseInt(br.readLine());

        for(int i = 0;i < n;i++){
            str = new StringTokenizer(br.readLine()," ");
            switch(str.nextToken()){
                case "push_front" :
                    deque.addFirst(Integer.parseInt(str.nextToken()));
                    break;

                case "push_back" :
                    deque.addLast(Integer.parseInt(str.nextToken()));
                    break;

                case "pop_front" :
                    if(!deque.isEmpty()) {
                        sb.append(deque.poll()).append('\n');
                    }else{
                        sb.append(-1).append('\n');
                    }
                    break;

                case "pop_back" :
                    if(!deque.isEmpty()) {
                        sb.append(deque.pollLast()).append('\n');
                    }else{
                        sb.append(-1).append('\n');
                    }
                    break;

                case "size" :
                    sb.append(deque.size()).append('\n');
                    break;

                case "empty" :
                    if(!deque.isEmpty()){
                        sb.append(0).append('\n');
                    }else{
                        sb.append(1).append('\n');
                    }
                    break;

                case "front" :
                    if(!deque.isEmpty()) {
                        sb.append(deque.peek()).append('\n');
                    }else{
                        sb.append(-1).append('\n');
                    }
                    break;

                case "back" :
                    if(!deque.isEmpty()) {
                        sb.append(deque.getLast()).append('\n');
                    }else{
                        sb.append(-1).append('\n');
                    }
                    break;
            }
        }

        System.out.println(sb);
    }
}
