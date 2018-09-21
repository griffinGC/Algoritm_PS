package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class numberSorting2 {
	public static void main(String[] args) throws Exception {
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader read = new BufferedReader(isr);
		
		
		int n = Integer.parseInt(read.readLine());
		int numbers[] = new int[n];
		for(int i = 0; i<n; i++) {
			numbers[i] = Integer.parseInt(read.readLine());
		}
		Arrays.sort(numbers);
		
		for(int i = 0; i<n; i++) {
			System.out.println(numbers[i]);
		}
		
		
	}
}
