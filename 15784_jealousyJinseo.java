package test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class jealousyJinseoRe {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String pro[] = str.split(" ");
		int number = Integer.parseInt(pro[0]);
		int row = Integer.parseInt(pro[1]) -1;
		int column = Integer.parseInt(pro[2]) -1;
		String strPro[][] = new String[number][number];
		for(int i = 0; i<number; i++) {
			str = br.readLine();
			//결국 2차원배열의 한 행에 들어가게됨 즉[][]여기서 뒤에것에 들어가게 됨
			strPro[i] = str.split(" ");  
		}
		int all[][] = new int[1][1];
		all[0][0] = Integer.parseInt(strPro[row][column]);
		for(int i = 0; i<number; i++) {
			if(all[0][0] < Integer.parseInt(strPro[i][column]))
			{
				System.out.println("ANGRY");
				return;
			}else if(all[0][0] < Integer.parseInt(strPro[row][i]))
			{
				System.out.println("ANGRY");
				return;
			}
		}
		System.out.println("HAPPY");
	}
}
