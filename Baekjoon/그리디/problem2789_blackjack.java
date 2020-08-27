package Baekjoon;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class problem2798_blackjack {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, m;
        n = sc.nextInt();
        m = sc.nextInt();
        int[] data = new int[n];
        for(int i = 0; i < n; i++) {
            data[i] = sc.nextInt();
        }
        int sum = 0;
        int max = 0;
        for(int i = 0; i < data.length-2; i++) {
            for(int j = i+1; j < data.length-1; j++) {
                for(int k = j+1; k < data.length; k++) {
                    sum = data[i] + data[j] + data[k];
                    if (sum <= m) {
                        max = Math.max(sum, max);
                    }
                }
            }
        }
        System.out.println(max);
    }
}
