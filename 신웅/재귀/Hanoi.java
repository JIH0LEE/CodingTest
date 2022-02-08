package 재귀;

import java.io.*;

public class Hanoi {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int count = 1;
        for(int i = 0;i < n;i++){
           count *= 2;
        }
        System.out.println(count - 1);
        Hanoi(n,1,3);
    }

    public static void Hanoi(int n,int start,int end){
        if(n == 0){
            return;
        }
        Hanoi(n-1,start,6-end-start);
        printMove(start, end);
        Hanoi(n-1,6-end-start,end);
    }

    public static void printMove(int a, int b){
        System.out.println(a + " " + b);
    }
}
