package 정렬;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 좌표압축 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int [] numbArr = new int [N];
        int [] sortedArr = new int [N];

        StringTokenizer str = new StringTokenizer(br.readLine());

        for(int i = 0;i < N;i++){
            numbArr[i] = Integer.parseInt(str.nextToken());
        }

        for(int i = 0;i < N;i++){
            sortedArr[i] = numbArr[i];
        }

        Arrays.sort(sortedArr);

        int val = 0;
        for(int i = 0;i < N;i++){
            val = numbArr[i];
            numbArr[i] = findSmall(val,sortedArr);
        }

        for(int i = 0;i < N;i++){
            bw.write(numbArr[i] + " ");
        }

        bw.flush();
        bw.close();
        br.close();
    }

    public static int findSmall(int value, int [] sortedA){
        int cnt = 0;
        if(sortedA.length >= 2) {
            if(sortedA[0] < value){
                cnt++;
            }

            for (int i = 1; i < sortedA.length; i++) {
                if ((value > sortedA[i]) && (sortedA[i] != sortedA[i - 1])) {
                    cnt++;
                }
            }
            return cnt;
        }else{
            return sortedA[0];
        }
    }
}
