package algorithm;
import java.util.Scanner;
public class GCDandLCM {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int a = scan.nextInt();
		int b = scan.nextInt();
		int big, small;
		if(a > b) {
			big = a;
			small = b;
		}else {
			big = b;
			small = a;
		}
		int gcdNumber = gcd(big,small);
		int lcmNumber = lcm(big, small); 
		System.out.println("gcd : " + gcdNumber);
		System.out.println("lcm : " + lcmNumber);
	}

	public static int gcd(int a, int b) {
		int temp;
		while(b > 0) {
//			temp = b; //잠시 여기저장 
//			b = a % b;
//			a = temp; 
			
			temp = a%b;
			a = b;
			b = temp;
		}
		return a;
	}
	public static int lcm(int big, int small) {
		int result = (big*small)/gcd(big,small);
		return result;
	}
}
