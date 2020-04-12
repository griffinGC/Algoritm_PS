package Baekjoon;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class problem2217_rope {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> ropeList = new ArrayList<Integer>();
        for(int i = 0; i<n; i++){
            ropeList.add(sc.nextInt());
        }
        Collections.sort(ropeList);
        int max = n * ropeList.get(0);
        for(int i = 0; i<n; i++){
            if(max < ropeList.get(i) * (n-i)){
                max = ropeList.get(i) * (n -i);
            }
        }
        System.out.println(max);
    }
}
