package 브루트포스;

import java.io.*;
import java.util.StringTokenizer;

public class 체스판칠하기 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int seroLength = Integer.parseInt(st.nextToken());
        int garoLength = Integer.parseInt(st.nextToken());

        char [][] board = new char [seroLength][garoLength];
        for (int i = 0;i < seroLength;i++){
            board[i] = br.readLine().toCharArray();
        }

        char [][] chess1 = new char [8][8];
        char [][] chess2 = new char [8][8];

        for(int i = 0;i < 8;i++){
            for(int j = 0;j < 8;j++){
                if((i + j)%2 == 1){
                    chess1[i][j] = 'B';
                    chess2[i][j] = 'W';
                }else{
                    chess1[i][j] = 'W';
                    chess2[i][j] = 'B';
                }
            }
        }

        int isSame1 = 0;
        int isSame2 = 0;
        int sameMax = 0;

        for(int i = 0;i <= seroLength - 8;i++){
            for(int j = 0;j <= garoLength - 8;j++){
                for(int k = 0;k < 8;k++){
                    for(int c = 0;c < 8;c++){
                        if(board[i+k][j+c] == chess1[k][c]){
                            isSame1++;
                        }
                        if(board[i+k][j+c] == chess2[k][c]){
                            isSame2++;
                        }
                    }
                }
                if((isSame1 >= sameMax)||(isSame2 >= sameMax)){
                    if(isSame1 >= isSame2){
                        sameMax = isSame1;
                    }else{
                        sameMax = isSame2;
                    }
                }
                isSame1 = 0;
                isSame2 = 0;
            }
        }

        System.out.println(64 - sameMax);
    }
}
