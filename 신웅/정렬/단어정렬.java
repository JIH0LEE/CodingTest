package 정렬;

import java.io.*;
import java.util.Arrays;
import java.util.Comparator;

public class 단어정렬 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        String [] strArr = new String [N];

        for(int i = 0;i < N;i++){
            strArr[i] = br.readLine();
        }

        Arrays.sort(strArr, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                if(o1.length() == o2.length()){
                    return o1.compareTo(o2);
                }else{
                    return o1.length() - o2.length();
                }
            }
        });

        bw.write(strArr[0] + "\n");
        for(int i = 1;i < N;i++){
            if(!strArr[i].equals(strArr[i-1])) {
                bw.write(strArr[i] + "\n");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
