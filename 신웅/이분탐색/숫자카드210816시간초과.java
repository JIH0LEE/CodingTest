package 이분탐색;
import java.io.*;
import java.util.StringTokenizer;
import java.util.Arrays;
public class 숫자카드210816시간초과 {
    static int N;
    static int M;
    static int[] nArr;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str;
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        nArr = new int[N];

        str = new StringTokenizer(br.readLine()," ");

        for(int i = 0;i < N;i++){
            nArr[i] = Integer.parseInt(str.nextToken());
        }

        M = Integer.parseInt(br.readLine());
        Arrays.sort(nArr);

        str = new StringTokenizer(br.readLine()," ");

        for(int i = 0;i < M;i++){
            int eng = Integer.parseInt(str.nextToken());
            int temp = binarySearch(0,N-1,eng);
            sb.append(rightBound(temp) + leftBound(temp) + 1).append(' ');
        }

        System.out.println(sb);
    }

    public static int binarySearch(int first,int last,int value){
        if(first <= last) {
            int mid = (first+last)/2;
            if (nArr[mid] == value) {
                return mid;
            } else if (nArr[mid] < value) {
                return binarySearch(mid + 1, last, value);
            } else {
                return binarySearch(first, mid - 1, value);
            }
        }
        return -1;
    }

    public static int rightBound(int index){
        if(index == -1){
            return 0;
        }
        int cnt = 0;
        while((index != N-1)&&(nArr[index] == nArr[index + 1])){
            cnt++;
            index++;
        }
        return cnt;
    }

    public static int leftBound(int index){
        if(index == -1){
            return -1;
        }
        int cnt = 0;
        while((index != 0)&&(nArr[index] == nArr[index - 1])){
            cnt++;
            index--;
        }
        return cnt;
    }
}
