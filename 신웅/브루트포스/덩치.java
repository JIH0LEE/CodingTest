package 브루트포스;

import java.util.Scanner;

public class 덩치 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int [] weightArr = new int [N];
        int [] heightArr = new int [N];
        int [] rankArr = new int [N];

        for(int i = 0;i < N;i++){
            weightArr[i] = sc.nextInt();
            heightArr[i] = sc.nextInt();
        }

        for(int k = 0;k < N;k++){
            rankArr[k] = 1;
        }

        for(int i = 0;i < N;i++){
            for(int j = 0;j < N;j++){
                if((i != j)&&(weightArr[i] < weightArr[j])&&(heightArr[i] < heightArr[j])){
                    rankArr[i]++;
                }
            }
        }

        for(int j = 0;j < N;j++){
            System.out.print(rankArr[j] + " ");
        }
    }
}
