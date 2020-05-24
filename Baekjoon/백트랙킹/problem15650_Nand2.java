package Baekjoon;

import java.util.Scanner;

public class problem15650_NandM2 {
    static boolean[] isUsed;
    static int[] arr;
    static int n;
    static int m;
    static void combination(int count, int min){
        if(count == m){
            printArray(arr);
            System.out.println();
            return ;
        }
        for(int i = min; i<n; i++){
            if(!isUsed[i]){
                arr[count] = i+1;
                isUsed[i] = true;
                combination(count+1, i+1);
                isUsed[i] = false;

            }
        }
    }

    static void printArray(int[] array){
        for(int ele : array){
            System.out.print(ele + " ");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        isUsed = new boolean[n];
        arr = new int[m];
        combination(0,0);
    }
}