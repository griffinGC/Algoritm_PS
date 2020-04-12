import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		int[] number = new int[5];
		Scanner scan = new Scanner(System.in);
		int sum = 0;
		for(int i =0 ; i<5; i++) {
			number[i] = scan.nextInt();
			if(number[i] < 40) {
				number[i] = 40;
			}
			sum += number[i];
		}
		int result = sum/5;
		System.out.println(result);
	}
}
