package algorithm;


import java.util.ArrayList;
import java.util.List;

public class countingSortImprove {

	static final int MAX = 50;
	public static void main(String[] args) throws Exception{
		
		int[] number = new int[] {5,5,3,4,5,1,0,4,1,3,0,2,4,2,3,0};
		int[] result = new int[number.length];
		//1을 추가해야 하는 이유 
		int[] count = new int[MAX];
		int[] countSum = new int[MAX];
		for(int i = 0; i < number.length; i++) {
			count[number[i]]++;
		}

		//여기에다가 -1을 해 줌으로써 배열에 0부터 넣을 수 있게 
		countSum[0] = count[0] -1;

		
		for(int i = 1; i<= 16; i++) {
			countSum[i] = count[i] + countSum[i-1];
		}

//		for(int i = 0; i< 10; i++) {
//			System.out.print(countSum[i] + " ");
//		}

		for(int i = number.length -1 ; i >= 0 ; i--) {
			 result[countSum[number[i]]]= number[i];
			 countSum[number[i]]--;
		}
		
		//result[0]에다가 저장
		System.out.println(result[0]);
		
		//이게 1에서 시작해서 15에서 끝남.
		for(int i = 0; i <= result.length -1; i++) {
			System.out.print(result[i] + " ");
		}
	}
}
