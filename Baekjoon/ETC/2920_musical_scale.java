package Baekjoon;

import java.util.Scanner;

public class problem2920_musical_scale {
    public static void main(String[] args) {
        int[] arr = new int[8];
        Scanner sc = new Scanner(System.in);
        for(int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        boolean asc = true;
        boolean desc = true;
        for(int i = 0; i < arr.length - 1; i++){
            if (arr[i] > arr[i+1]){
                asc = false;
            }
            if (arr[i] < arr[i+1]){
                desc = false;
            }
        }
        if (asc) {
            System.out.println("ascending");
        } else if (desc) {
            System.out.println("descending");
        } else {
            System.out.println("mixed");
        }
    }
}
