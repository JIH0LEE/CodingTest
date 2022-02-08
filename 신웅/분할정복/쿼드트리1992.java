package 분할정복;
import java.io.*;
import java.util.StringTokenizer;

public class 쿼드트리1992 {
    static int[][] video;
    static int videoSize;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        videoSize = Integer.parseInt(br.readLine());
        video = new int[videoSize][videoSize];

        for(int i=0;i<videoSize;i++){
            String str = br.readLine();
            for(int j=0;j<videoSize;j++){
                video[i][j] = Character.getNumericValue(str.charAt(j));
            }
        }

        recursive(0,0,videoSize);
        System.out.println(sb);
    }

    public static void recursive(int x, int y,int size){
        if(size == 1){
            if(video[y][x] == 1){
                sb.append(1);
            }else{
                sb.append(0);
            }
        }else{
            int sum = 0;
            for(int i =y;i < y+size;i++){
                for(int j =x;j < x+size;j++){
                    sum += video[i][j];
                }
            }

            if(sum == size*size){
                sb.append(1);
            }else if(sum == 0){
                sb.append(0);
            }else{
                sb.append('(');
                recursive(x,y,size/2);
                recursive(x+size/2,y,size/2);
                recursive(x,y+size/2,size/2);
                recursive(x+size/2,y+size/2,size/2);
                sb.append(')');
            }
        }
    }
}