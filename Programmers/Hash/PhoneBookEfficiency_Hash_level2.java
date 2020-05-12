package Programmers;

import java.util.Arrays;

public class PhoneBookEfficiency_Hash_level2 {
    static boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        for(int i = 0; i<phone_book.length-1; i++){
            if(phone_book[i+1].contains(phone_book[i])) return false;
        }
        boolean answer = true;
        return answer;
    }

    public static void main(String[] args) {
        String[] pb = {"119", "97674223", "1195524421"};
        String[] pb2 = {"123","456","789"};
        String[] pb3 = {"88","123","1235","567","12"};
        System.out.println(solution(pb));
        System.out.println(solution(pb2));
        System.out.println(solution(pb3));
    }
}
