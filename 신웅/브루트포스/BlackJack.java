package 브루트포스;

import java.util.Scanner;

public class BlackJack {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int [] nArr = new int [N];
        for(int i =0;i < N;i++){
            nArr[i] = sc.nextInt();
        }
        int min = M;
        int finalValue = 0;

        for(int i = 0;i < N-2;i++){
            for (int j = i + 1; j < N-1; j++) {
                for(int k = j + 1;k < N;k++){
                    if((Math.abs(M - nArr[i] - nArr[j] - nArr[k]) <= min) && (nArr[i] + nArr[j] + nArr[k] <= M)){
                        min = Math.abs(M - nArr[i] - nArr[j] - nArr[k]);
                        finalValue = nArr[i] + nArr[j] + nArr[k];
                    }
                }
            }
        }

        System.out.println(finalValue);

    }
}
