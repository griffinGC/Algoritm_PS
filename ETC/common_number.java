package algorithm;

import java.util.Scanner;

public class sw_1204 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int number = scan.nextInt();
		for(int i = 0; i<number; i++) {
			int pNumber = scan.nextInt();
			int total[] = new int[101];
			for(int j = 0; j<1000; j++) {
				int temp = scan.nextInt();
				for(int k = 0; k<102;k++) {
					if(temp == k)
					{
						total[k]++;
					}	
				}	
			}
			int max = total[0];
			int mNumber = 0;
			for(int j = 0; j<total.length; j++) {
				if(max <= total[j]) {
					max = total[j];
					mNumber = j;
				}
			}
//			System.out.println(mNumber);
//			System.out.println("77의 값 : " +total[77]);
//			System.out.println("79의 값 : " +total[79]);
			
			System.out.println("#"+pNumber+ " "+mNumber);
		}
	}
}
