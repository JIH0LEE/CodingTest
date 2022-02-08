package 재귀;

import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numb;

        numb = scanner.nextInt();

        System.out.println(factorial(numb));
    }

    public static int factorial(int n){
        if(n == 0){
            return 1;
        }else if(n == 1){
            return 1;
        }else{
            return factorial(n - 1) * n;
        }
    }
}
