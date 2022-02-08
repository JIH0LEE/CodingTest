package 재귀;

import java.util.Scanner;

public class 별찍기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numb = sc.nextInt();

        char [][] pointArr = new char [numb][numb];

        for(int i = 0;i < numb;i++)
            for(int j = 0;j < numb;j++){
                pointArr[i][j] = ' ';
            }

        pointStar(0,0,pointArr,numb);

        for(int i=0;i<pointArr.length;i++) {
            System.out.println(pointArr[i]);
        }
    }

    public static void pointStar(int x, int y, char[][] A, int length){
        if(length == 1){
            A[x][y] = '*';
        }else{
            for(int i = 0;i < 3;i++)
                for(int j = 0;j < 3;j++){
                    if(!(i == 1 && j == 1)){
                        pointStar(x + i*(length/3),y + j*(length/3),A,length/3);
                    }
                }
        }
    }
}
