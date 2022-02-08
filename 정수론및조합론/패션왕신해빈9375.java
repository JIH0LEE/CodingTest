package 정수론및조합론;
import java.io.*;
import java.util.HashMap;
import java.util.StringTokenizer;

public class 패션왕신해빈9375 {
    static int numb;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int cnt = 0;
        while(cnt++ < n){
            HashMap<String,Integer> hm = new HashMap<String,Integer>();

            numb = Integer.parseInt(br.readLine());

            for(int i = 0;i < numb;i++){
                StringTokenizer str = new StringTokenizer(br.readLine());
                str.nextToken();
                String item = str.nextToken();

                if(hm.containsKey(item)){
                    hm.put(item,hm.get(item)+1);
                }else{
                    hm.put(item,1);
                }
            }

            int result = 1;
            for(int val : hm.values()){
                result *= (val+1);
            }

            System.out.println(result-1);
        }
    }
}
