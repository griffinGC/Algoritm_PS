package practice;

import java.util.Iterator;
import java.util.LinkedList;

public class dfs {
	public static void main(String[] args) {
		Graph gp = new Graph(5);
		gp.insertEdge(1, 2);
		gp.insertEdge(1, 3);
		gp.insertEdge(1, 4);
		gp.insertEdge(2, 4);
		gp.insertEdge(3, 4);
		gp.DFS(1);

	}
}

class Graph {
	private int V;
	//보통 LinkedList<ArrayList<Integer>> 를 사용해도 되지만 배열을 사용해서 인접리스트 구현함.
	private LinkedList<Integer> adj[]; 
	
	public Graph(int v) {
		V = v;
		adj = new LinkedList[v];
		for(int i = 0; i< v; i++) {
			adj[i] = new LinkedList();
		}
	}
	
	void insertEdge(int n, int m) { 
		adj[n].add(m);//양방향을 굳이 할 필요가 없음
		//한노드에서만 인접리스트를 가지도록 만듬 

	}

	//노드 검색 
	void Search(int root, boolean visited[]) {
		visited[root] = true;
		System.out.print(root + " ");
		
		Iterator<Integer> itr = adj[root].listIterator();
		while(itr.hasNext()) {
			int n = itr.next();
			if(!visited[n])
			{
				//스택대신에 재귀함수를 이용함 
				Search(n, visited);
			}
		}
	}

	void DFS(int v) {//DFS를 특정 V라는 노드에서 시작
		//처음에 모두 false라는 값을 가짐 
		boolean visited[] = new boolean[V];
		Search(v, visited);
	}
	
}
