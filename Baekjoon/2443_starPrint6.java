import java.util.Scanner;

public class starPrint {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int number = scan.nextInt();
		int k = 2*number - 1; //별 초기화 
		int s = 0;//공백 초기화 
		while(number > 0)
		{
			//공백의 숫자를 지정하고 그 숫자동안 반복 
			for(int i = 0; i<s; i++) {
				System.out.print(" ");
			}
			//바로 가져다 쓰면 계속 초기화 되기 때문에 여기서 변경해줌
			int m = k;
 
			//별의 갯수동안 찍어줌 
			while(m > 0) {
					System.out.print("*");
					m--;
				}
			System.out.println();
			s++;
			number --;
			k -=2;
		}

	}
}
