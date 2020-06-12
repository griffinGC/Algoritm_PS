package Baekjoon;

import java.util.Scanner;

public class problem10872_factorial {
    static int factorialFunction(int n){
        if(n ==1 || n == 0){
            return 1;
        }else{
            return n*factorialFunction(n-1);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(factorialFunction(n));
    }
}
