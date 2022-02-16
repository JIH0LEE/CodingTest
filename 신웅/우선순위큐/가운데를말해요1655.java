package 우선순위큐;
import java.io.*;
import java.util.Collections;
import java.util.PriorityQueue;

public class 가운데를말해요1655 {
    static int N;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> bigHeap = new PriorityQueue<>();
        PriorityQueue<Integer> smallHeap = new PriorityQueue<>(Collections.reverseOrder());
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        int num1 = Integer.parseInt(br.readLine());
        sb.append(num1).append('\n');
        if(N >= 2) {
            int smallCnt = 0;
            int bigCnt = 0;
            int num2 = Integer.parseInt(br.readLine());
            if (num1 <= num2) {
                smallHeap.offer(num1);
                smallCnt++;
                bigHeap.offer(num2);
                bigCnt++;
            } else {
                smallHeap.offer(num2);
                smallCnt++;
                bigHeap.offer(num1);
                bigCnt++;
            }
            sb.append(smallHeap.peek()).append('\n');
            int mid = smallHeap.peek();
            for (int i = 0; i < N - 2; i++) {
                num1 = Integer.parseInt(br.readLine());
                if(num1 >= mid){
                    if(smallCnt == bigCnt){
                        smallHeap.offer(num1);
                        smallCnt++;
                        mid = smallHeap.peek();
                    }else if(smallCnt > bigCnt){
                        bigHeap.offer(num1);
                        bigCnt++;
                        mid = smallHeap.peek();
                    }else if(smallCnt < bigCnt){
                        smallHeap.offer(bigHeap.poll());
                        smallCnt++;
                        bigCnt--;
                        bigHeap.offer(num1);
                        bigCnt++;
                        mid = smallHeap.peek();
                    }
                }else{
                    if(smallCnt == bigCnt){
                        smallHeap.offer(num1);
                        smallCnt++;
                        mid = smallHeap.peek();
                    }else if(smallCnt > bigCnt){
                        bigHeap.offer(smallHeap.poll());
                        smallCnt--;
                        bigCnt++;
                        smallHeap.offer(num1);
                        smallCnt++;
                        mid = smallHeap.peek();
                    }
                }
                sb.append(mid).append('\n');
            }
        }
        System.out.println(sb);
    }
}
