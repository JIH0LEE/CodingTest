package 정렬;

import java.io.*;

public class 수정렬하기3 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] cntArr = new int[10001];
        int input = Integer.parseInt(br.readLine());

        int value=0;
        for(int i=0; i<input; i++) {
            value = Integer.parseInt(br.readLine());
            cntArr[value]++;
        }

        int cnt=0;
        for(int i=1; i<=10000; i++) {
            for(int j=0; j<cntArr[i]; j++) {
                bw.write(i+"\n");
                cnt++;
            }
            if(cnt==input)
                break;
        }
        bw.flush();

        br.close();
        bw.close();
    }
}