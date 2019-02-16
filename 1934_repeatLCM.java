package algorithm;

import java.util.Scanner;

public class LCMRepeat {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int rNumber = scan.nextInt();
		for(int i = 0; i<rNumber; i++) {
			int number1 = scan.nextInt();
			int number2 = scan.nextInt();
			int big, small, result;
			if(number1 > number2) {
				big = number1; small = number2;
			}
			else {
				big = number2; small = number1;
			}
			result = lcm(big, small);
			System.out.println(result);
		}
	}
	
	public static int gcd(int big, int small) {
		if(big % small == 0)
		{
			return small;
		}
		return gcd(small, big%small);
	}
	public static int lcm(int big, int small) {
		return (big * small)/gcd(big, small);
	}
}
