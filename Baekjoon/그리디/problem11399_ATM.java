package Baekjoon;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class problem11399_ATM {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i = 0; i<n; i++){
            list.add(sc.nextInt());
        }
        Collections.sort(list);
        int cur = 0;
        int result = 0;
        int finalResult=0;
        int before = 0;
        for(int i = 0; i<n; i++){
            cur = list.get(i);
            result = before + cur;
            finalResult += result;
            before = result;
        }
        System.out.println(finalResult);
    }
}
