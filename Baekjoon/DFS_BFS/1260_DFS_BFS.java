package algorithm;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;

public class boj_1260_DFS_BFS_new {
	
	static boolean[] visit ;
	static LinkedList[] adj ;
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int number, edgeN, root;
		number = scan.nextInt();
		edgeN = scan.nextInt();
		root = scan.nextInt();
		int n, m;
		//인접리스트 생성 
        adj = new LinkedList[number+1];
        //방문여부 체크하기 위해서 생성 초기값은 false
        visit = new boolean[number + 1];
        //노드번호가 1부터 시작하기 때문에 이렇게 설정
        for(int i = 1; i<=number; i++) {
			adj[i] = new LinkedList<Integer>();
		}
		for(int i = 0; i<edgeN; i++)
		{
			n = scan.nextInt();
			m = scan.nextInt();
			adj[n].add(m);
			adj[m].add(n);
		}
		//방문가능한 노드가 여러개인경우 작은것부터 방문하기 위해서 소트함 
		for(int i = 1; i<=number; i++) {
			Collections.sort(adj[i]);
		}
		dfs(root);
		visit = new boolean[number+1];
		System.out.println();
		bfs(root);

	}
	public static void dfs(int root) {
        if(visit[root])return;
		visit[root] = true;
		System.out.print(root + " ");
		Iterator<Integer> itr = adj[root].iterator();
		while(itr.hasNext()) {
			int s = itr.next();
			if(!visit[s]) {
				dfs(s);
			}
		}
	}
	public static void bfs(int root) {
		LinkedList<Integer> q = new LinkedList<Integer>();
		visit[root] = true;
		q.add(root);
		while(q.size() != 0)
		{
			int temp = q.poll();
			System.out.print(temp + " ");
			Iterator<Integer> itr = adj[temp].iterator();
			while(itr.hasNext()) {
				int i = itr.next();
				if(!visit[i])
				{
					visit[i] = true;
					q.add(i);
				}
			}
		}
		
	}
}
