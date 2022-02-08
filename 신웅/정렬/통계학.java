package 정렬;

import java.io.*;
import java.util.Arrays;

public class 통계학 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int [] numbArr = new int [N];

        for(int i = 0;i < N;i++){
            numbArr[i] = Integer.parseInt(br.readLine());
        }

        int avg = 0;
        int center = 0;
        int mostVal = 0;
        float sum = 0;
        int range = 0;

        for(int i = 0;i < N;i++){
            sum += numbArr[i];
        }

        avg = Math.round(sum/N);

        Arrays.sort(numbArr);

        center = numbArr[N/2];

        range = numbArr[N - 1] - numbArr[0];

        int [] count = new int [range + 1];
        int [] cIndex = new int [range + 1];
        int cnt = 0;
        int index = 0;
        int max = 0;

        if(N >= 2) {
            for (int i = 0; i < N; i++) {
                if (i != N - 1) {
                    while ((i+1 <N)&&(numbArr[i] == numbArr[i + 1])) {
                        cnt++;
                        i++;
                    }
                    cIndex[index] = numbArr[i];
                    count[index] = cnt + 1;
                    cnt = 0;
                    index++;
                } else {
                    if (numbArr[N - 1] != numbArr[N - 2]) {
                        cIndex[index] = numbArr[N - 1];
                        count[index] = 1;
                    } else {
                        break;
                    }
                }
            }


            for (int i = 0; i <= range; i++) {
                if (count[i] > max) {
                    max = count[i];
                }
            }

            int mostCount = 0;
            for (int i = 0; i <= range; i++) {
                if (count[i] == max) {
                    mostCount++;
                }
            }

            int[] countIndex = new int[mostCount];
            int index1 = 0;

            for (int i = 0; i <= range; i++) {
                if (count[i] == max) {
                    countIndex[index1] = cIndex[i];
                    index1++;
                }
            }

            if (mostCount > 1) {
                mostVal = countIndex[1];
            }else{
                mostVal = countIndex[0];
            }


        }else{
            mostVal = numbArr[0];
        }
        bw.write(avg + "\n");
        bw.write(center + "\n");
        bw.write(mostVal + "\n");
        bw.write(range + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}
