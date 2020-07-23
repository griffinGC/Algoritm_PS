package Programmers.PerfectSearch;

import java.util.*;

public class FindPrime_level2 {
    public static void main(String[] args) {
        String number1 = "71"; // 3;
        String number2 = "011"; //2;
        int result1 = solution(number1);
        int result2 = solution(number2);
        System.out.println("result1 : " + result1);
        System.out.println("result2 : " + result2);
    }
    static int solution(String numbers){
        int answer = 0;
        String[] strArr = numbers.split("");
        int[] numArr = new int[strArr.length];
        for(int i = 0; i<numArr.length; i++){
            numArr[i] = Integer.parseInt(strArr[i]);
        }
        Set<Integer> set = new HashSet<>();
        for(int i = 1; i<=numArr.length; i++){
            permutation(strArr, 0, i, set);
        }
        answer = set.size();
        return answer;
    }
    static void permutation(String[] arr, int depth, int k, Set<Integer> set){
        if(depth == k){
            print(arr, k, set);
            return;
        }
        for(int i = depth; i<arr.length; i++){
            swap(arr, i, depth);
            permutation(arr, depth+1, k, set);
            swap(arr, i, depth);
        }
    }
    static void print(String[] arr, int k, Set<Integer> set){
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i<k ; i++){
            sb.append(arr[i]);
        }
        checkPrime(Integer.parseInt(sb.toString()), set);
    }
    static void checkPrime(int number, Set<Integer> set){
        boolean check = false;
        if(number <= 1){
            return;
        }
        for(int i = 2; i<=Math.sqrt(number); i++){
            if(number % i == 0){
                check = true;
                break;
            }
        }
        if(!check){
            set.add(number);
        }
    }
    static void swap(String[] arr, int i, int depth){
        String temp = arr[i];
        arr[i] = arr[depth];
        arr[depth] = temp;
    }

}