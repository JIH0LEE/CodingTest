package 정수론및조합론;
import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class 배수와약수5086 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayList<Integer> arr1 = new ArrayList<Integer>();
        ArrayList<Integer> arr2 = new ArrayList<Integer>();
        String s = br.readLine();
        while(!s.equals("0 0")){
            StringTokenizer str = new StringTokenizer(s," ");
            print(Integer.parseInt(str.nextToken()),Integer.parseInt(str.nextToken()));
            s = br.readLine();
        }
    }

    public static boolean isFactor(int a, int b){
        if(b % a == 0){
            return true;
        }else{
            return false;
        }
    }

    public static boolean isMultiple(int a, int b){
        if(a % b == 0){
            return true;
        }else{
            return false;
        }
    }

    public static void print(int a, int b){
        if(isFactor(a,b)){
            System.out.println("factor");
        }
        else if(isMultiple(a,b)){
            System.out.println("multiple");
        }
        else{
            System.out.println("neither");
        }
    }
}
