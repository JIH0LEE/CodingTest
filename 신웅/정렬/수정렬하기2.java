package 정렬;

import java.io.*;
import java.util.Arrays;

public class 수정렬하기2 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        int [] numbArr = new int [N];


        for(int i = 0;i < N;i++){
            numbArr[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(numbArr);

        for(int i : numbArr){
            bw.write(i + "\n");
        }
        bw.flush();
        bw.close();


        /* 퀵소트 시간초과
        quickSort(numbArr,0,numbArr.length - 1);

        for(int i = 0;i < N;i++){
            System.out.println(numbArr[i]);
        }
        */
    }




    /*
    public static void quickSort(int [] A,int start, int end){
        int part = partition(A,start,end);
        if(start < part - 1){
            quickSort(A,start,part - 1);
        }
        if(end > part){
            quickSort(A,part,end);
        }
        return;
    }

    public static int partition(int [] A, int start, int end){
        int pivot = A[(start + end)/2];
        while(start <= end){
            while(A[start] < pivot){
                start++;
            }
            while(A[end] > pivot){
                end--;
            }
            if(start <= end){
                swap(A,start,end);
                start++;
                end--;
            }
        }
        return start;
    }

    public static void swap(int[] A, int a,int b){
        int temp;
        temp = A[a];
        A[a] = A[b];
        A[b] = temp;
        return;
    }
    */


}
