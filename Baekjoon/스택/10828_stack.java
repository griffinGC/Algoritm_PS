package algorithm;

import java.util.Scanner;
import java.util.Stack;

public class stack_10828 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int number = scan.nextInt();
		Stack <Integer> stk = new Stack<Integer>();
		for(int i = 0; i <number; i++) {
			String menu = scan.next();
			if(menu.equals("push")) 
			{
				int pNumber = scan.nextInt();
				stk.push(pNumber);
			}
			else if(menu.equals("top")) 
			{
				if(stk.empty()) {
					System.out.println("-1");
				}else {
					System.out.println(stk.peek());
				}				
			}
			else if(menu.equals("pop")) 
			{
				if(stk.empty())
				{
					System.out.println("-1");
				}else {
					System.out.println(stk.pop());	
				}	
			}
			else if(menu.equals("size")) 
			{
				System.out.println(stk.size());
			}
			else if(menu.equals("empty")) 
			{
				if(stk.empty()) {
					System.out.println("1");
				}else {
					System.out.println("0");
				}
			}
		}
	}
}
