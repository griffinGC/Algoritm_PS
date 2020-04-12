package Baekjoon;

import java.util.Scanner;

public class problem1541_lost_bracket_upgrade {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        int result = 0;
        String temp = "";
        boolean minus = false;
        for(int i = 0; i<=a.length(); i++){
            if(i == a.length() || a.charAt(i) == '+' || a.charAt(i) == '-' ){
                if(minus)
                    result += -Integer.parseInt(temp);
                else
                    result += Integer.parseInt(temp);
                temp = "";
                if(i != a.length() && a.charAt(i) == '-') minus = true;
                continue;
            }
            temp = temp + a.charAt(i);
        }
        System.out.println(result);
    }
}
