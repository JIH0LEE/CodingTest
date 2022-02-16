package 우선순위큐;
import java.io.*;
import java.util.Comparator;
import java.util.PriorityQueue;

public class 절댓값힙11286 {
    static int N;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        PriorityQueue<Integer> queue = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                if(Math.abs(o1) > Math.abs(o2)){
                    return 1;
                }else if(Math.abs(o1) == Math.abs(o2)){
                    return o1-o2;
                }else{
                    return -1;
                }
            }
        });
        N = Integer.parseInt(br.readLine());
        int num = 0;
        for(int i = 0;i < N;i++){
            num = Integer.parseInt(br.readLine());
            if(num == 0){
                if(!queue.isEmpty()){
                    sb.append(queue.poll()).append('\n');
                }else{
                    sb.append(0).append('\n');
                }
            }else{
                queue.offer(num);
            }
        }

        System.out.println(sb);
    }
}
