package algorithm;

public class fastMaxSum {

	public static void main(String[] args) {


	}
	
	public int fastMaxSum(int[] a) {
		int n = a.length;
		int result = 0;
		int sum = 0;
		for(int i = 0; i< n; ++i) {
			sum = Math.max(sum, 0) + a[i];
			result = Math.max(sum, result);
		}
		//maxAt[i] = max(0, maxAt[i-1]) + a[i]
		return result;
		
	}

}
