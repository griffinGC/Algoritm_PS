package algorithm;

import java.util.Scanner;

public class collatz {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
//		int i = in.nextInt();
		int j = in.nextInt();
		int result = 0;
		int flag = 1;
		
//		while(result != i)
		result = j;
		while(result != 1)
		{
			if(result %2 == 0) {
				result = result /2;
				flag++;
			}
			else {
				result = 3*result + 1;
				flag++;
			}
		}
		System.out.println(flag);

	}

}
