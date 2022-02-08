package 정수론및조합론;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 팩토리얼0의개수1676 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int cnt = 0;
        int result = 0;
        int addval = 0;
        int temp = 0;
        while(cnt <= n){
            addval = 0;
            temp = cnt;
            while(temp != 0){
                if(temp % 5 == 0){
                    temp /= 5;
                    addval++;
                }else{
                    break;
                }
            }
            cnt++;
            result += addval;
        }

        System.out.println(result);
    }
}
