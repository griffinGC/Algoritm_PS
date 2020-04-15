package algorithm;

import java.util.Scanner;

public class collatzUpgrade {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int i = in.nextInt();//최소 수 입력 받음
		int j = in.nextInt();//최대 수 입력 받음
		int result = 0;
		int flag = 1;
		int max = 0;
		result = j;
		while(i<=j)//i와 j사이 계산
		{
			result = i;
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
			i++;
			if(max < flag)
			{
				max = flag;
			}
			flag = 1; //초기화
		}
		System.out.println(max);
	}
}
