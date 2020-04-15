package Baekjoon;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class problem_10610_30 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 숫자가 굉장히 클수 있어서 오류 고려해야함
        String number = sc.nextLine();
        // 각 숫자의 갯수의 합이 3의 배수가 된다면 그것은 3의 배수이다.
        // 가장 큰 수를 만드는 것이니 Sorting 하면 됨
        ArrayList<Integer> nList = new ArrayList<>();
        int sum = 0, each = 0;
        for(int i = 0; i<number.length(); i++){
            each = (int) number.charAt(i) - '0';
            nList.add(each);
            sum += each;
        }
        if(sum % 3 == 0 && nList.contains(0)){
            Collections.sort(nList, (a,b) -> {return b - a;});
            for(Integer ele : nList){
                System.out.print(ele);
            }
        }else{
            System.out.println("-1");
        }
    }
}
