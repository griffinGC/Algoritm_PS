package Programmers;

import java.util.Arrays;

public class greedy_workout_level1 {
    public static int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int arr[] = new int[n+1];
        for(int i = 0; i<lost.length; i++) arr[lost[i]]--;
        for(int i = 0; i<reserve.length; i++) arr[reserve[i]]++;
        System.out.println(Arrays.toString(arr));
        for(int i = 1; i<=n; i++){
            // 앞의 값과 비교하는것이 먼저 나와야 함
            if(arr[i] >0 && i-1 > 0 && arr[i-1] <0){
                arr[i]--;
                arr[i-1]++;
                System.out.println("after i : " + i);
            }
            if(arr[i] >0 && i<n && arr[i+1] <0){
                arr[i]--;
                arr[i+1]++;
                System.out.println("before i : " + i);
            }
        }
        System.out.println(Arrays.toString(arr));
        for(int i = 1; i<=n; i++){
            if(arr[i] >=0){
                answer++;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        int n = 5;
//        int n = 3;
//        int n = 6;
//        int n = 24;
//        int n = 18;
        int[] lost = {2, 4};
//        int[] lost = {1,3,4,5};
//        int[] lost = {12, 13, 16, 17, 19, 20, 21, 22};
//        int[] lost = {7,8,11,12};
//        int[] lost = {3};
        int[] reserve = {1,3,5};
//        int[] reserve = {1,4};
//        int[] reserve = {1,22, 16, 18, 9, 10};
//        int[] reserve = {1,6,8,10};
//        int[] reserve = {3};
//        int[] reserve = {1};
        int answer = solution(n, lost, reserve);
        System.out.println("answer : " + answer);
    }
}
