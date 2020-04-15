package Baekjoon;

import java.util.*;

public class problem1946_new_employee {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int caseN = sc.nextInt();
        for(int i = 0; i < caseN; i++){
            TreeMap<Integer, Integer> score = new TreeMap<>();
            int n = sc.nextInt();
            for(int j = 0; j<n; j++){
                int a = sc.nextInt();
                int b = sc.nextInt();
                score.put(a, b);
            }
            int min = n + 1, cnt = 0;
            Iterator<Integer> itr = score.keySet().iterator();
            while(itr.hasNext()){
                Integer key = itr.next();
                Integer value = score.get(key);
//                System.out.println("key : " + key + " / value : " + value);
                if(min > value){
                    cnt++;
                    min = value;
                }
            }
            System.out.println(cnt);
        }
    }
}

