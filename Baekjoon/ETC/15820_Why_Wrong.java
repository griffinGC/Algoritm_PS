import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int samN, sysN;
		samN = scan.nextInt();
		sysN = scan.nextInt();
		int flag1 = 0;
		int flag2 = 0;
		for(int i = 0 ; i < samN; i++) {
			int fNum = scan.nextInt();
			int sNum = scan.nextInt();
			if(fNum != sNum) {
				flag1 += 1;
			}
			fNum = 0; sNum = 0;
		}
		for(int i = 0; i < sysN; i++) {
			int fNum = scan.nextInt();
			int sNum = scan.nextInt();
			if(fNum != sNum) {
				flag2 += 1;
			}
		}
		if((flag1 == 0) && (flag2 == 0)) {
			System.out.println("Accepted");
			return;
		}else if(flag1 != 0) {
			System.out.println("Wrong Answer");
			return;
		}else if((flag1 == 0) && (flag2 != 0)) {
			System.out.println("Why Wrong!!!");
			return;
		}		
	}
}
