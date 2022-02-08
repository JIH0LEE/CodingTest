package 큐덱;
import java.io.*;
import java.util.LinkedList;
import java.util.Queue;

public class 카드22164 {
    static int N;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Queue<Integer> queue = new LinkedList<>();

        N = Integer.parseInt(br.readLine());

        for(int i = 1;i <= N;i++){
            queue.offer(i);
        }

        for(int i = 0;i < N-1;i++){
            queue.remove();
            queue.offer(queue.poll());
        }

        System.out.println(queue.peek());
    }
}
