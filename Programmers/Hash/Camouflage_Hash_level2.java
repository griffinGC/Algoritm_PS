package Programmers;

import java.util.*;

public class Camouflage_Hash_level2 {
    static int solution(String[][] clothes) {
        HashMap<String, Integer> hash = new HashMap<>();

        for(int i = 0; i<clothes.length; i++) {
            hash.put(clothes[i][1], hash.getOrDefault(clothes[i][1], 0)+1);
        }

        int answer = 1;
        // 각각의 독립된 사건이기 때문에 곱하기를 해줌
        // +1 의 경우 안쓸수도 있기 때문
        for(int val : hash.values()){
            answer *= (val+1);
        }
        // -1을 해주는 것은 모두가 안쓰는 경우는 없기 때문
        return answer - 1;
    }
    public static void main(String[] args) {
        String[][] clothes = {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
        System.out.println(solution(clothes));
    }
}
