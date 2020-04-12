package algorithm;


import java.util.ArrayList;
import java.util.List;

public class countingSort {

	static final int MAX = 50;
	public static void main(String[] args) throws Exception{
		
		int[] number = new int[] {5,5,3,4,5,1,0,4,1,3,0,2,4,2,3,0};
		int[] result = new int[number.length+1];
		//1을 추가해야 하는 이유 
		int[] count = new int[MAX];
		int[] countSum = new int[MAX];
		for(int i = 0; i < number.length; i++) {
			count[number[i]]++;
		}

		//제대로 들어감
		countSum[0] = count[0];
		//ok
		
		for(int i = 1; i<= 16; i++) {
			countSum[i] = count[i] + countSum[i-1];
		}
		//ok
		//애초에 countSum을 할때 16까지 되기 때문에 result에 1을 추가해 줘야함.
		//즉 총 숫자의 개수자체가 16개가 들어가기 때문에 고려해 줘야함.
		for(int i = 0; i< 10; i++) {
			System.out.print(countSum[i] + " ");
		}

		for(int i = number.length -1 ; i >= 0 ; i--) {
			 result[countSum[number[i]]]= number[i];
			 countSum[number[i]]--;
		}
		
		//result[0]에다가 저장을 하지 않고 끝남.
		System.out.println(result[0]);
		
		//이게 1에서 시작해서 15에서 끝남.
		for(int i = 1; i <= result.length -1; i++) {
			
			System.out.print(result[i] + " ");
		}
		
		
	}
}
