package 큐덱;
import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 요세푸스문제011866 {
    static int N;
    static int K;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(str.nextToken());
        K = Integer.parseInt(str.nextToken());

        Queue<Integer> queue = new LinkedList<>();
        for(int i = 1;i <= N;i++){
            queue.offer(i);
        }

        sb.append('<');

        int cnt = 1;
        while(!queue.isEmpty()){
            if(queue.size() == 1){
                sb.append(queue.poll());
            }else {
                if (cnt % K == 0) {
                    sb.append(queue.poll()).append(',').append(' ');
                } else {
                    queue.offer(queue.poll());
                }
                cnt++;
            }
        }

        sb.append('>');

        System.out.println(sb);
    }
}
