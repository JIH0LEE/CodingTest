package 분할정복;
import java.io.*;
import java.util.StringTokenizer;

public class 색종이만들기2630 {
    static int arrSize;
    static byte[][] colorPaper;
    static int blueCnt=0;
    static int whiteCnt=0;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str;

        arrSize = Integer.parseInt(br.readLine());

        colorPaper = new byte[arrSize][arrSize];

        for(int i = 0;i < arrSize;i++){
            str = new StringTokenizer(br.readLine()," ");
            for(int j = 0;j < arrSize;j++){
                colorPaper[i][j] = Byte.parseByte(str.nextToken());
            }
        }

        recursive(0,0,arrSize);
        System.out.println(whiteCnt);
        System.out.println(blueCnt);
    }

    public static void recursive(int x, int y, int size){
        if(size == 1){
            if(colorPaper[x][y] == 0){
                whiteCnt++;
            }else{
                blueCnt++;
            }
        }else {
            int sum = 0;
            for (int i = x; i < x + size; i++) {
                for (int j = y; j < y + size; j++) {
                    sum += colorPaper[i][j];
                }
            }

            if (sum == size * size) {
                blueCnt++;
            } else if (sum == 0) {
                whiteCnt++;
            } else {
                recursive(x, y, size / 2);
                recursive(x + size / 2, y, size / 2);
                recursive(x, y + size / 2, size / 2);
                recursive(x + size / 2, y + size / 2, size / 2);
            }
        }
    }
}
