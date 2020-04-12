package Baekjoon;

import java.lang.reflect.Array;
import java.util.*;

public class problem1260_dfs_bfs {

    public static ArrayList<Integer> dfsFunction(ArrayList<ArrayList<Integer>> adj, int start, int n){
        ArrayList<Integer> dfsOrder = new ArrayList<Integer>();
        Stack<Integer> dfsStack = new Stack<Integer>();
        ArrayList<Boolean> visited = new ArrayList<Boolean>(Arrays.asList(new Boolean[n+1]));
        Collections.fill(visited, Boolean.FALSE);

        dfsStack.add(start);

        while(!dfsStack.isEmpty()){
            int cur = dfsStack.pop();
            if(visited.get(cur)){
                continue;
            }
            visited.set(cur, true);
            dfsOrder.add(cur);
            for(int i = adj.get(cur).size() - 1; i>=0; i--){
                int connectedNode = adj.get(cur).get(i);
                if(!visited.get(connectedNode)){
                    dfsStack.add(connectedNode);
                }
            }
        }
        return dfsOrder;
    }

    public static ArrayList<Integer> bfsFunction(ArrayList<ArrayList<Integer>> adj, int start, int n){
        ArrayList<Integer> bfsOrder = new ArrayList<Integer>();
        ArrayList<Boolean> visited = new ArrayList<Boolean>(Arrays.asList(new Boolean[n+1]));
        Collections.fill(visited, Boolean.FALSE);
        Queue<Integer> bfsQueue = new LinkedList<Integer>();

        bfsQueue.add(start);

        while(!bfsQueue.isEmpty()){
            int cur = bfsQueue.poll();
            if(visited.get(cur)){
                continue;
            }
            visited.set(cur, true);
            bfsOrder.add(cur);
            for(int i = 0; i<adj.get(cur).size(); i++){
                int connectedNode = adj.get(cur).get(i);
                if(!visited.get(connectedNode)){
                    bfsQueue.add(connectedNode);
                }
            }
        }
        return bfsOrder;
    }

    public static void main(String[] args) {
        int node, edge, start;
        Scanner sc = new Scanner(System.in);
        node = sc.nextInt();
        edge = sc.nextInt();
        start = sc.nextInt();

        ArrayList<ArrayList<Integer>> adj = new ArrayList<ArrayList<Integer>>();
        for(int i = 0; i<=node; i++){
            adj.add(new ArrayList<Integer>());
        }

        for(int i = 0; i<edge; i++){
            int u,v;
            u = sc.nextInt();
            v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        for(int i = 0; i<=node; i++){
            Collections.sort(adj.get(i));
        }

        ArrayList<Integer> dfsResult = dfsFunction(adj, start, node);
        ArrayList<Integer> bfsResult = bfsFunction(adj, start, node);

        for(int ele : dfsResult){
            System.out.print(ele + " ");
        }
        System.out.println();
        for(int ele : bfsResult){
            System.out.print(ele + " ");
        }
    }
}
