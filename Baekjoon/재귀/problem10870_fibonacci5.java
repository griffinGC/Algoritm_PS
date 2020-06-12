package Baekjoon;

import java.util.Scanner;

public class problem10870_fibonacci5 {
    static int fibonacci5(int n ){
        if(n == 0){
            return 0;
        }else if(n == 1){
            return 1;
        }
        return fibonacci5(n-1) + fibonacci5(n-2);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int result = fibonacci5(n);
        System.out.println(result);
    }
}
