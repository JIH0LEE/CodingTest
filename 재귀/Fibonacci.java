package 재귀;

import java.util.Scanner;

public class Fibonacci {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numb;
        numb = scanner.nextInt();
        System.out.println(fibonacci(numb + 1));
    }

    public static int fibonacci(int n){
        if(n == 1){
            return 0;
        }else if(n == 2){
            return 1;
        }else{
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
    }
}
