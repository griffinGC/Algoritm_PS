package algorithm;

import java.util.Scanner;

public class boj_2455_intelligenceTrain {
	public static void main(String[] args) {
		Scanner scan  = new Scanner(System.in);
		int inN, outN;
		int preN = 0;
		int max = 0;
		for(int i = 0 ; i < 4; i++) {
			inN = scan.nextInt();
//			System.out.println("input 값 : " + inN);
			outN = scan.nextInt();
//			System.out.println("output 값 : " + outN);
			preN = preN - inN + outN;
//			System.out.println("현재 값 : " + preN);
			if(max < preN) {
				max = preN;
			}
		}
		System.out.println(max);
	}
}
