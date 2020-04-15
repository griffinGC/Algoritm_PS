package Baekjoon;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class problem2437_balances {
    public static void main(String[] args) {
        // 값을 정렬 한 후, 오름차순으로 더하기 시작해서
        // 더한 값 + 1 이 다음으로 더해야 할 값보다 작으면 break;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> aList = new ArrayList<>();
        for(int i = 0; i<n; i++){
            int number = sc.nextInt();
            aList.add(number);
        }
        Collections.sort(aList);
        int sum = 1;
        for(int i = 0; i<aList.size(); i++){
            if(sum < aList.get(i)) break;
            sum += aList.get(i);
        }
        System.out.println(sum);
    }
}
