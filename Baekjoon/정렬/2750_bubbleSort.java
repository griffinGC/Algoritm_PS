import java.io.BufferedReader;
import java.io.InputStreamReader;

public class bubbleSort {
	public static void main(String[] args) throws Exception{
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader bsr = new BufferedReader(isr);
		
		int n = Integer.parseInt(bsr.readLine());
		int number[] = new int[n];
		for(int i = 0; i<n; i++) {
			number[i] = Integer.parseInt(bsr.readLine());
		}
		for(int i = 0; i<n-1; i++) {
			for(int j = i+1; j<n; j++) {
				if(number[i] > number[j]) {
					int temp = number[i];
					number[i] = number[j];
					number[j] = temp;
				}
			}
		}
		
		for(int i = 0; i<n; i++) {
			System.out.println(number[i]);
		}
	}
}
