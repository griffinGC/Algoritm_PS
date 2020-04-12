package Baekjoon;

import java.util.Scanner;
import java.util.Stack;

public class problem11047_coin {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, k;
        int result = 0;
        n = sc.nextInt();
        k = sc.nextInt();
        Stack<Integer> stk = new Stack<Integer>();
        for(int i = 0; i<n; i++){
            stk.push(sc.nextInt());
        }
        for(int i = 0; i<n; i++){
            int num = stk.pop();
            if(num > k){
                continue;
            }
            result += k / num;
            k = k % num;
        }
        System.out.println(result);
    }
}
