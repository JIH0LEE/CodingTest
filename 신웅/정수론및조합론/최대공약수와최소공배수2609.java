package 정수론및조합론;
import java.util.Scanner;
public class 최대공약수와최소공배수2609 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int initb = b;
        int inita = a;

        int gcd = 0;
        int lcm = 0;

        int tempa = 0;
        int tempb = 0;
        while(true){
            if(a%b == 0){
                gcd = b;
                break;
            }

            tempb = b;
            tempa = a;

            a = tempb;
            b = tempa % tempb;
        }

        lcm = (inita*initb)/gcd;

        System.out.println(gcd);
        System.out.println(lcm);
    }
}
