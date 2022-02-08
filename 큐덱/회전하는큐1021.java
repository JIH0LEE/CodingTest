package 큐덱;
import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class 회전하는큐1021 {
    static int N;
    static int M;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(br.readLine()," ");
        LinkedList<Integer> deque = new LinkedList<>();

        N = Integer.parseInt(str.nextToken());
        M = Integer.parseInt(str.nextToken());

        for(int i = 1;i <= N;i++){
            deque.offer(i);
        }

        str = new StringTokenizer(br.readLine()," ");

        int totalCnt = 0;

        for(int i = 0;i < M;i++){
            int tempCnt = 0;
            int target = Integer.parseInt(str.nextToken());
            int location = deque.indexOf(target);

            if(location > deque.size() - location){
                tempCnt = deque.size() - location;
                for(int j = 0;j < tempCnt;j++){
                    deque.offerFirst(deque.pollLast());
                }
                deque.poll();
            }else{
                tempCnt = location;
                for(int j = 0;j < tempCnt;j++){
                    deque.offerLast(deque.poll());
                }
                deque.poll();
            }

            totalCnt += tempCnt;
        }

        System.out.println(totalCnt);
    }
}
