package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class boj_9012_bracket {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int number = Integer.parseInt(br.readLine());
		while(number-- >0) {
			Stack stk = new Stack();
			String str = br.readLine();
			char temp;
			for(int i = 0; i<str.length(); i++) {
				temp = str.charAt(i);
				// '('와 같은게 들어가면 스택에 넣는다 만약에 다른게 들어오면 pop한다.
				if(temp == '(')
					{stk.push(temp);}
				else {
					//비엇을경우 예외처리 아무거나 넣어줌 
					if(stk.isEmpty()) {
						stk.push('f');
						break;
					}
					stk.pop();
				}
			}
			//비어있다는것은 제대로 다 뽑혔다는 것을 의미함. 그래서 비어있다면 yes 출력 
			if(stk.isEmpty()){
				System.out.println("YES");
			//무언가 남아있다면 잘못 됬다는 것을 의미하므로 no출력 
			}else {
				System.out.println("NO");
				}			
		}
	}
}
