package practice;

import java.util.Iterator;
import java.util.LinkedList;

public class bfs {
	public static void main(String[] args) {
		GraphBFS bfs = new GraphBFS(5);
		bfs.addEdge(1, 2);
		bfs.addEdge(1, 3);
		bfs.addEdge(1, 4);
		bfs.addEdge(2, 4);
		bfs.addEdge(3, 4);
		bfs.BFS(1);
	}
}

class GraphBFS{
	private int V;
	private LinkedList<Integer> adj[];
	
	public GraphBFS(int v) {
		V = v;
		adj = new LinkedList[v];
		for(int i = 0; i< v; i++) {
			//배열과 링크드리스트를 이용해서 인접리스트 생성함 
			adj[i] = new LinkedList();
		}
	}
	
	//노드추가 
	public void addEdge(int n, int m) { adj[n].add(m); }
	
	public void BFS(int s) {
		boolean visited[] = new boolean[V];
		LinkedList<Integer> queue = new LinkedList();
		visited[s] = true;
		queue.add(s);
		
		while(queue.size() != 0)
		{
			//큐에서 하나를 뽑아옴 
			s = queue.poll();
			System.out.print(s + " ");
		
			//인접리스트에 다음것 있을때까지 계속 뽑아옴 
			Iterator<Integer> itr = adj[s].iterator();
			while(itr.hasNext())
			{
				int i = itr.next();
				if(!visited[i])
				{
					visited[i] = true;
					queue.add(i);
				}
			}
		}
	}
}
