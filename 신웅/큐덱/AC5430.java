package 큐덱;
import java.io.*;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class AC5430 {
    static int tcNum;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        LinkedList<Integer> deque = new LinkedList<>();
        StringTokenizer str;

        tcNum = Integer.parseInt(br.readLine());

        for (int i = 0; i < tcNum; i++) {
            String function = br.readLine();
            int deqSize = Integer.parseInt(br.readLine());

            String value = br.readLine();
            str = new StringTokenizer(value, ",");

            if (deqSize == 0) {
                deque.clear();
            } else if (deqSize == 1) {
                deque.offer(Character.getNumericValue(value.charAt(1)));
            } else {
                deque.offer(Character.getNumericValue(str.nextToken().charAt(1)));
                for (int j = 0; j < deqSize - 2; j++) {
                    deque.offer(Integer.parseInt(str.nextToken()));
                }
                deque.offer(Character.getNumericValue(str.nextToken().charAt(0)));
            }
            for (int j = 0; j < function.length(); j++) {
                if (function.charAt(j) == 'R') {
                    R(deque);
                } else {
                    if (deque.isEmpty()) {
                        sb.append("error").append('\n');
                        break;
                    } else {
                        deque.poll();
                    }
                }
            }

            if (!deque.isEmpty()) {
                sb.append('[');
                int dequeSize = deque.size();
                for (int j = 0; j < dequeSize - 1; j++) {
                    sb.append(deque.poll()).append(',');
                }
                sb.append(deque.poll()).append(']').append('\n');
            }

            deque.clear();
        }

        System.out.println(sb);
    }

    public static void R(LinkedList<Integer> ll) {
        Queue<Integer> temp = new LinkedList<>();
        int llLength = ll.size();
        for (int i = 0; i < llLength; i++) {
            temp.offer(ll.pollLast());
        }

        int tempLength = temp.size();
        for (int i = 0; i < tempLength; i++) {
            ll.addLast(temp.poll());
        }
    }
}
