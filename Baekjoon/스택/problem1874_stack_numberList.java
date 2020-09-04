package stackAlgorithm;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;

public class problem1874_stack_numberList {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int count = 1;
        List<Character> result = new ArrayList<>();
        Stack<Integer> stk = new Stack<>();
        for(int i = 1; i <= n; i++) {
            int data = sc.nextInt();
            while(data >= count) {
                stk.push(count);
                count++;
                result.add('+');
            }
            if(stk.peek() == data){
                stk.pop();
                result.add('-');
            } else {
                System.out.println("NO");
                return;
            }
        }
        for(int i = 0; i < result.size(); i++) {
            System.out.println(result.get(i));
        }
    }
}
