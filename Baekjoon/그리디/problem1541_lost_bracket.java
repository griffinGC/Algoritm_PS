package Baekjoon;

import java.util.Scanner;

public class problem1541_lost_bracket {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String sent = sc.nextLine();
        int startIdx = 0, endIdx = 0, result = 0, number = 0;
        boolean isMinus = false;
        for(int i = 0; i<sent.length(); i++){
            char now = sent.charAt(i);
            if(now == '-' || now == '+' || i+1 == sent.length()){
                if(i + 1 == sent.length()){
                    endIdx = i+1;
                }else{
                    endIdx = i;
                }
            }else{
                continue;
            }
            String temp = sent.substring(startIdx, endIdx);
            startIdx = i+1;
            number = Integer.parseInt(temp);
            if(isMinus){
                result -= number;
            }else{
                result += number;
            }
            if(!isMinus && now == '-'){
                isMinus = true;
            }
        }
        System.out.println(result);
    }
}