package 브루트포스;

import java.util.Scanner;

public class 영화감독숌 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int rank = 0;
        int numb = 1;
        int compNum = 1;
        int answer = 0;

        while(rank < N){
            while (true){
                if(numb % 10 == 6){
                    if((numb/10) % 10 == 6){
                        if((numb/100) % 10 == 6){
                            rank++;
                            answer = compNum;
                            break;
                        }
                    }
                }
                numb /= 10;
                if(numb == 0){
                    break;
                }
            }
            compNum++;
            numb = compNum;
        }
        System.out.println(answer);
    }
}
