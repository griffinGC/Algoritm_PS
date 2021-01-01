package Baekjoon;

import java.util.*;

public class problem2606_virus {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int node = sc.nextInt();
        int edge = sc.nextInt();
        ArrayList<ArrayList<Integer>> list = new ArrayList<>();
        for(int i = 0; i<node; i++){
            list.add(new ArrayList<>());
        }
        for(int i = 0; i<edge; i++){
            int n1 = sc.nextInt() -1;
            int n2 = sc.nextInt() -1;
            list.get(n1).add(n2);
            list.get(n2).add(n1);
        }
        int answer = bfs(list, node);
        System.out.println(answer);
    }
    public static int bfs(ArrayList<ArrayList<Integer>> list, int nodeNumber){
        int answer = 0;
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[nodeNumber];
        // 원래 1번이지만 원래노드 -1 상태이기 때문에 0부터 시작!
        q.add(0);
        while(!q.isEmpty()){
            int current = q.poll();
            if(visited[current] == true){
                continue;
            }
            answer++;
            visited[current] = true;
            for(int i = 0; i< list.get(current).size(); i++){
                int f = list.get(current).get(i);
                if(visited[f] == false){
                    q.add(f);
                }
            }
        }
        return answer -1 ;
    }
}