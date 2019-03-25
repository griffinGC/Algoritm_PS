package dfs;

import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;

public class virus {
	static LinkedList[] cList;
	static boolean[] visited;
	static int flag = 0;
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int nNumber = scan.nextInt();
		int eNumber = scan.nextInt();
		cList = new LinkedList[nNumber+1];	
		for(int i = 1; i<=nNumber; i++) {
			cList[i] = new LinkedList<Integer>();
		}
		int n, m;
		visited = new boolean[nNumber+1];
		for(int i = 0; i<eNumber; i++) {
			n = scan.nextInt();
			m = scan.nextInt();
			cList[m].add(n);
			cList[n].add(m);
		}
		for(int i = 1; i<=nNumber; i++) {
			Collections.sort(cList[i]);
		}
		wSearch(1);
		//처음 들어가는 1은 제외해야하니까 -1 해서 flag개수를 출력함.
		System.out.print(flag -1);

	}
	//dfs이용함 
	static void wSearch(int v){
		if(visited[v] == true) return;
		visited[v] = true;
//		System.out.print(v + " ");
		flag ++;
		Iterator<Integer> itr = cList[v].iterator();
		while(itr.hasNext()) {
			int next = itr.next();
			if(visited[next] != true) {
				wSearch(next);
			}
		}
		
	}
}
