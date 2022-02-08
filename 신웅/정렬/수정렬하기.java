package 정렬;

import java.io.*;

public class 수정렬하기 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int [] numbArr = new int [N];

        for(int i = 0;i < N;i++){
            numbArr[i] = Integer.parseInt(br.readLine());
        }

        int temp = 0;

        for(int i = 0;i < N - 1;i++){
            for(int j = i + 1;j <= N - 1;j++){
                if(numbArr[i] > numbArr[j]){
                    temp = numbArr[i];
                    numbArr[i] = numbArr[j];
                    numbArr[j] = temp;
                }
            }
        }

        for(int i = 0;i < N;i++){
            System.out.println(numbArr[i]);
        }
    }
}
