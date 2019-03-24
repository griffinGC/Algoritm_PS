import java.util.Scanner;

public class hawkEyes {
	public static void main(String[] args) {
		int a = 10;
		int b = 100;
		int list[] = {10, 0, 0, 100};
		Scanner scan = new Scanner(System.in);
		String str = scan.nextLine();
		String line[] = str.split("");
		for(int i = 0; i<line.length; i++) {
			if(line[i].equals("A"))
			{
				A(list);
			}else if(line[i].equals("B"))
			{
				B(list);
			}else if(line[i].equals("C"))
			{
				C(list);
			}else if(line[i].equals("D"))
			{
				D(list);
			}else if(line[i].equals("E"))
			{
				E(list);
			}else if(line[i].equals("F"))
			{
				F(list);
			}
		}
		int s= 0,l = 0;
		for(int i = 0; i<4; i++) {
			if(list[i] == 10)
			{
				s = i+1;
			}else if(list[i]== 100) {
				l = i+1;
			}
		}
		System.out.println(s);
		System.out.println(l);
	}
	
	static void A(int[] list) {
		int temp;
		temp = list[0];
		list[0] = list[1];
		list[1] = temp;
	}
	static void B(int[] list) {
		int temp;
		temp = list[2];
		list[2] = list[0];
		list[0] = temp;
	}
	static void C(int[] list) {
		int temp;
		temp = list[3];
		list[3] = list[0];
		list[0] = temp;
	}
	static void D(int[] list) {
		int temp;
		temp = list[1];
		list[1] = list[2];
		list[2] = temp;
	}
	static void E(int[] list) {
		int temp;
		temp = list[1];
		list[1] = list[3];
		list[3] = temp;
	}
	static void F(int[] list) {
		int temp;
		temp = list[2];
		list[2] = list[3];
		list[3] = temp;
	}
}
