package 큐덱;
import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 프린터큐1966 {
    static int tcNumb;
    static int docuNumb;
    static int rank;
    static LinkedList<int[]> ll = new LinkedList<>();
    static int[] cntBig;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer str;

        tcNumb = Integer.parseInt(br.readLine());

        int cnt = 0;
        for(int i = 0;i < tcNumb;i++){
            str = new StringTokenizer(br.readLine()," ");
            docuNumb = Integer.parseInt(str.nextToken());
            rank = Integer.parseInt(str.nextToken());

            str = new StringTokenizer(br.readLine()," ");
            for(int j = 0;j < docuNumb;j++){
                ll.offer(new int[] {j, Integer.parseInt(str.nextToken())});
            }

            while(!ll.isEmpty()){
                int[] front = ll.poll();
                boolean isMax = true;
                for(int j = 0;j < ll.size();j++){
                    if(front[1] < ll.get(j)[1]){
                        isMax = false;
                        break;
                    }
                }

                if(isMax == true){
                    cnt++;
                    if(front[0] == rank){
                        break;
                    }
                }else{
                    ll.offer(front);
                }
            }
            sb.append(cnt).append('\n');
            cnt = 0;
            ll.clear();
        }

        System.out.println(sb);
    }
}
