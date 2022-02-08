package 정렬;

import java.io.*;
import java.util.Arrays;
import java.util.Collections;

public class 소트인사이드 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String s = br.readLine();

        String numbArr [] = s.split("");

        Arrays.sort(numbArr, Collections.reverseOrder());   //내림차순정렬

        for(int i = 0;i < numbArr.length;i++){
            System.out.print(numbArr[i]);
        }
    }
}
