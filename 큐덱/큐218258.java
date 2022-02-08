package 큐덱;
import java.util.*;
import java.io.*;

public class 큐218258 {
    public static void main(String [] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        final int n = Integer.parseInt(br.readLine());
        Deque<Integer> dq = new ArrayDeque<Integer>();

        for(int i=0;i<n;i++) {
            st = new StringTokenizer(br.readLine());
            String order = st.nextToken();
            switch(order) {
                case "push" :
                    int num  = Integer.parseInt(st.nextToken());
                    dq.push(num);
                    break;

                case "pop" :
                    if(dq.isEmpty()) {
                        sb.append(-1);
                    }else {
                        sb.append(dq.pollLast());
                    }
                    sb.append("\n");
                    break;

                case "size" :
                    sb.append(dq.size());
                    sb.append("\n");
                    break;

                case "empty" :
                    if(dq.isEmpty()) {
                        sb.append(1);
                    }else {
                        sb.append(0);
                    }
                    sb.append("\n");
                    break;

                case "front" :
                    if(dq.isEmpty()) {
                        sb.append(-1);
                    }else {
                        sb.append(dq.peekLast());
                    }
                    sb.append("\n");
                    break;
                case "back" :
                    if(dq.isEmpty()) {
                        sb.append(-1);
                    }else {
                        sb.append(dq.peekFirst());
                    }
                    sb.append("\n");
                    break;
            }
        }

        sb.append("\n");

        bw.write(sb.toString());

        bw.flush();
        br.close();
        bw.close();

    }


}