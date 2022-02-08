package 분할정복;
import java.io.*;
import java.util.StringTokenizer;

public class 종이의개수1780 {
    static int[][] paper;
    static int paperSize;
    static int minusOneCnt=0;
    static int zeroCnt=0;
    static int oneCnt=0;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        paperSize=Integer.parseInt(br.readLine());
        paper=new int[paperSize][paperSize];
        StringTokenizer str;
        for(int i=0;i<paperSize;i++){
            str = new StringTokenizer(br.readLine()," ");
            for(int j=0;j<paperSize;j++){
                paper[i][j] = Integer.parseInt(str.nextToken());
            }
        }

        recursive(0,0,paperSize);
        System.out.println(minusOneCnt);
        System.out.println(zeroCnt);
        System.out.println(oneCnt);
    }

    public static void recursive(int x,int y,int size){
        if(size == 1){
            if(paper[y][x] == -1){
                minusOneCnt++;
            }else if(paper[y][x] == 0){
                zeroCnt++;
            }else{
                oneCnt++;
            }
        }else{
            boolean minusOneComp = true;
            boolean zeroComp = true;
            boolean oneComp = true;
            for(int i=y;i<y+size;i++){
                for(int j=x;j<x+size;j++){
                    if(paper[i][j] == -1){
                        zeroComp = false;
                        oneComp = false;
                    }else if(paper[i][j] == 0){
                        minusOneComp = false;
                        oneComp = false;
                    }else{
                        minusOneComp = false;
                        zeroComp = false;
                    }
                }
            }
            if(minusOneComp == true){
                minusOneCnt++;
            }else if(zeroComp == true){
                zeroCnt++;
            }else if(oneComp == true){
                oneCnt++;
            }else{
                recursive(x,y,size/3);
                recursive(x+size/3,y,size/3);
                recursive(x+size*2/3,y,size/3);
                recursive(x,y+size/3,size/3);
                recursive(x+size/3,y+size/3,size/3);
                recursive(x+size*2/3,y+size/3,size/3);
                recursive(x,y+size*2/3,size/3);
                recursive(x+size/3,y+size*2/3,size/3);
                recursive(x+size*2/3,y+size*2/3,size/3);
            }
        }
    }
}
