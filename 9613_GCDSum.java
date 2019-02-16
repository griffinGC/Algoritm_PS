package algorithm;

import java.util.Scanner;

public class GCDSum {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int rNumber = scan.nextInt();
		for(int i = 0; i< rNumber; i++) 
		{
			int totalNumber = scan.nextInt();
			int total[] = new int[totalNumber];
			for(int j = 0; j<totalNumber; j++) {
				total[j] = scan.nextInt();
			}
			long sum = 0;
			for(int j = 0; j<total.length - 1; j++) 
			{
				for(int k = j+1; k<total.length; k++) 
				{
					int temp = gcd(total[j], total[k]);
					sum += temp;
				}
			}
			System.out.println(sum);
		}
	}
	
	public static int gcd(int number1, int number2) {
		if(number1 < number2)
		{
			int temp = number1;
			number1 = number2;
			number2 = temp;
		}
		if(number2 == 0) {
//			System.out.println("number1의 값 : " + number1);
//			System.out.println("number2의 값 : " + number2);
			return number1;
		}
//		System.out.println("number1의 값 : " + number1);
//		System.out.println("number2의 값 : " + number2);
		return gcd(number2, number1%number2);
	}
}
