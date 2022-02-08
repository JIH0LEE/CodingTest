package 브루트포스;

import java.util.Scanner;

public class 분해합 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numb = sc.nextInt();

        int sum = 0;
        int answer = 0;
        int inum = -1;
        for(int i = 0;i < numb;i++){
            inum = i;
            while(inum != 0){
                 sum += inum % 10;
                 inum = inum / 10;
             }
             if(sum == numb - i){
                 answer = i;
                 break;
             }else{
                 answer = 0;
             }
             sum = 0;
        }

        System.out.println(answer);

    }
}
