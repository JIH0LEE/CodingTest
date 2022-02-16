package 우선순위큐;
import java.io.*;
import java.util.Collections;
import java.util.PriorityQueue;

public class 최대힙11279 {
    static int N;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        N = Integer.parseInt(br.readLine());
        int num = 0;
        for(int i = 0;i < N;i++){
            num = Integer.parseInt(br.readLine());
            if(num == 0){
                if(!queue.isEmpty()){
                    sb.append(queue.poll()).append('\n');
                    continue;
                }else{
                    sb.append(0).append('\n');
                    continue;
                }
            }
            queue.offer(num);
        }

        System.out.println(sb);
    }
}
