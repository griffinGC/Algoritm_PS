import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
public class Main {
	public static void main(String[] args) throws Exception {
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader bufread = new BufferedReader(isr);
		int n = Integer.parseInt(bufread.readLine());
		int[] count = new int[n];
		for(int i =0; i<n; i++) {
			count[i] = Integer.parseInt(bufread.readLine());
		}
		Arrays.sort(count);
		for(int i= 0; i<count.length; i++) {
			System.out.println(count[i]);			
		}
	}
}
