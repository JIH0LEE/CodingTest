package 분할정복;
import java.io.*;
import java.util.StringTokenizer;

public class 랜선자르기1654 {
    static int K;
    static int N;
    static long[] arr;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str;
        str = new StringTokenizer(br.readLine()," ");
        K = Integer.parseInt(str.nextToken());
        N = Integer.parseInt(str.nextToken());
        long max = 0;
        arr = new long[K];
        for(int i = 0;i < K;i++){
            arr[i] = Integer.parseInt(br.readLine());
            if(arr[i] > max){
                max = arr[i];
            }
        }

        System.out.println(binarySearch(0,max+1)-1);
    }
    public static long binarySearch(long start, long last){
        while(start < last){
            long mid = (start+last)/2;
            if(N > count(mid)){
                last = mid;
            }else{
                start = mid+1;
            }
        }
        return start;
    }

    public static long count(long value){
        long cnt = 0;
        for(int i = 0;i < K;i++){
            cnt += arr[i]/value;
        }

        return cnt;
    }
}
