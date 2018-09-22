package algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class insertionSort {
	public static void main(String[] args) throws Exception{
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader bfr = new BufferedReader(isr);
		
		int input = Integer.parseInt(bfr.readLine());
		int number[] = new int[input];
		for(int i = 0; i < input; i++) {
			number[i] = Integer.parseInt(bfr.readLine());
		}
		
		int key;
		int k;
		for(int i = 1; i<input; i++) {
			key = number[i];
			k = i - 1;
			while(k >=0 && number[k] > key)
			{
				number[k+1] = number[k];
				k = k-1;
			}
			number[k+1] = key;
		}
		
		for(int i = 0; i<input; i++) {
			System.out.println(number[i]);
		}
		
	}
}
