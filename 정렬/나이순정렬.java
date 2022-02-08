package 정렬;

import java.io.*;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class 나이순정렬 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        String [][] user = new String [N][3];

        for(int i = 0;i < N;i++){
            StringTokenizer str = new StringTokenizer(br.readLine());
            user[i][0] = str.nextToken();
            user[i][1] = str.nextToken();
            user[i][2] = String.valueOf(i);
        }

        Arrays.sort(user, new Comparator<String[]>() {
            @Override
            public int compare(String[] o1, String[] o2) {                      //왜 equals와 compareTo 사용했을때 안되는지 모르겠음.
                if(Integer.parseInt(o1[0]) == Integer.parseInt(o2[0])){
                    return Integer.parseInt(o1[2]) - Integer.parseInt(o2[2]);
                }else{
                    return Integer.parseInt(o1[0]) - Integer.parseInt(o2[0]);
                }
            }
        });

        for(int i = 0;i < N;i++){
            bw.write(user[i][0] + " " + user[i][1] + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
