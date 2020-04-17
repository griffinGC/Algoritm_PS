package Baekjoon;

import java.util.*;

public class problem2606_virus_upgrade {
    public static int result = 0;
    public static boolean[] visited;
    public static void search(ArrayList<ArrayList<Integer>> arList, int v){
        if(visited[v] == true) return;
        visited[v] = true;
        result++;
        for(int next : arList.get(v)){
            if(visited[next] == false){
                search(arList, next);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int node = sc.nextInt();
        int edge = sc.nextInt();
        ArrayList<ArrayList<Integer>> list = new ArrayList<>();
        for(int i = 0; i<node; i++){
            list.add(new ArrayList<>());
        }
        visited = new boolean[node];
        for(int i = 0; i<edge; i++){
            int n1 = sc.nextInt() -1;
            int n2 = sc.nextInt() -1;
            list.get(n1).add(n2);
            list.get(n2).add(n1);
        }
        search(list, 0);
        System.out.println(result-1);
    }
}