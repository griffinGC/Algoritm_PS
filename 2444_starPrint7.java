import java.util.Scanner;

public class starPrint7 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int number = scan.nextInt();
		int starN = 0;
		int spaceN = number -1;

		for (int i = 1; i <=number; i++) {
			int nSpace = spaceN;
			while(nSpace > 0) {
				System.out.print(" ");
				nSpace--;
			}
			spaceN--;
			starN = i*2 -1;
			while(starN > 0) {
				System.out.print("*");
				starN--;
			}
			System.out.println();
		}
	
		int sSpaceN = 1;
		for(int i = number-1; i > 0; i--) {
			int nSpace = sSpaceN;
			while(nSpace > 0) {
				System.out.print(" ");
				nSpace--;
			}
			sSpaceN++;
			starN = i*2 -1;
			while(starN > 0) {
				System.out.print("*");
				starN--;
			}
			System.out.println();
		}
	}
}
