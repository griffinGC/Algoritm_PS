package Baekjoon;

import java.util.Scanner;

public class proglem2003_sum_of_numbers_2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] list = new int[n];
        for(int i = 0; i<n; i++){
            list[i] = sc.nextInt();
        }
        int end = 0, count = 0, sum = 0;
        for(int i = 0; i<n; i++){
            while(sum < m && end < n){
                sum += list[end];
                end++;
            }
            if(sum == m){
                count++;
            }
            sum -= list[i];
        }
        System.out.println(count);
    }
}
