package Programmers.Heap;

import java.util.Collections;
import java.util.PriorityQueue;

public class RamenFactory_level2 {
    static int solution(int stock, int[] dates, int[] supplies, int k) {
        int answer = 0;
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
        int dateCount = 0;
        for(int i = 0; i<k; i++){
            if(dateCount < dates.length && i == dates[dateCount]){
                priorityQueue.add(supplies[dateCount]);
                dateCount++;
            }
            if(stock == 0){
                stock += priorityQueue.poll();
                answer++;
            }
            stock--;
        }
        return answer;
    }
    public static void main(String[] args) {
        int stock = 4;
        int[] dates = {4, 10, 15};
        int[] supplies = {20, 5, 10};
        int k = 30;
        int result = solution(stock, dates, supplies, k);
        System.out.println(result);
    }
}
