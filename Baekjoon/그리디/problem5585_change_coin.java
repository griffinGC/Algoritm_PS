package Baekjoon;

import java.util.Scanner;

public class problem5585_change_coin {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int money = sc.nextInt();
        money = 1000 - money;
        int n = 0;
        n += money / 500;
        money = money % 500;

        n += money / 100;
        money = money % 100;

        n += money / 50;
        money = money % 50;

        n += money / 10;
        money = money % 10;

        n += money / 5;
        money = money % 5;

        n += money / 1;
        money = money % 1;

        System.out.println(n);
    }
}
