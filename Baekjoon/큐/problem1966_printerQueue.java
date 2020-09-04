package QueueAlgorithm;

import java.util.*;

public class problem1966_printerQueue {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for(int i = 0; i < tc; i++){
            int n = sc.nextInt();
            int m = sc.nextInt();
            Queue<Node> q = new LinkedList<>();
            PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
            for(int j = 0; j<n; j++){
                int value = sc.nextInt();
                q.add(new Node(j, value));
                pq.add(value);
            }
            int count = 0;
            while(true) {
                Node getNode = q.poll();
                if(pq.peek() == getNode.value) {
                    count++;
                    pq.poll();
                    if(getNode.number == m) {
                        System.out.println(count);
                        break;
                    }
                } else {
                    q.add(getNode);
                }
            }
        }
    }
}
class Node {
    public int number;
    public int value;
    Node(int number, int value) {
        this.number = number;
        this.value = value;
    }
}
