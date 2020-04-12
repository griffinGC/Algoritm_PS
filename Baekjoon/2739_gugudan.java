package algorithm;

import java.util.Scanner;

public class boj_2739_gugudan {
	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
		int n = scn.nextInt();
		for(int i = 1; i<=9; i++) {
			System.out.println(n + " * " + i +" = "+ n*i );
		}
	}
}
