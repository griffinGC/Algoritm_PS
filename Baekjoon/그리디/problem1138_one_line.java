package Baekjoon;

import java.util.*;

public class problem1138_one_line {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] oneLine = new int[n];
        for(int i = 1; i<=n; i++){
            int number = sc.nextInt();
            int count = 0;
            for(int j = 0; j<n; j++){
                if(oneLine[j] == 0 && count == number){
                    oneLine[j] = i;
                    break;
                }
                if(oneLine[j] == 0) count++;
            }
        }
        for(int i = 0; i<n; i++){
            System.out.print(oneLine[i] + " ");
        }

    }
}
