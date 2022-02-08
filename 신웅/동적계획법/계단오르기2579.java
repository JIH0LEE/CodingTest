package 동적계획법;

import java.io.*;

public class 계단오르기2579 {
    static int [] stairs;
    static int N;
    static Integer [] partialSum;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        stairs = new int[N + 1];
        stairs[0] = 0;
        for (int i = 0; i < N; i++) {
            stairs[i + 1] = Integer.parseInt(br.readLine());
        }

        partialSum = new Integer [N+1];
        partialSum[0] = 0;
        partialSum[1] = stairs[1];

        if(N >= 2) {
            partialSum[2] = stairs[1] + stairs[2];
        }
        System.out.println(optimalSum(N));

    }

    public static int optimalSum(int stairsNum){
        if(partialSum[stairsNum] == null){
            partialSum[stairsNum] = Math.max(optimalSum(stairsNum - 2),
                    optimalSum(stairsNum - 3) + stairs[stairsNum - 1]) + stairs[stairsNum];
        }
        return partialSum[stairsNum];
    }
}
