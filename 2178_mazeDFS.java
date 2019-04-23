package dfs;

import java.util.AbstractMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Stack;

public class mazeboj2178_renewal {
	static int maze[][];
	static boolean visited[][];
	static int row;
	static int column;
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		row = scan.nextInt();
		column = scan.nextInt();
		String temp;
		maze= new int[row][column];
		visited = new boolean[row][column];
		for(int i = 0; i<row ;i++) 
		{
			temp = scan.next();
			for(int j = 0; j<column; j++)
			{
				if((temp.charAt(j) - '0') == 1)
					{visited[i][j] = true;}
				else {
					visited[i][j] = false;
				}
				maze[i][j] = Integer.MAX_VALUE;
			}
		}
		
		//x,y좌표 2개를 넣기 위해 key, value를 가진 map사용 
		Stack<Map.Entry<Integer,Integer>> stk = new Stack<Map.Entry<Integer,Integer>>();
		stk.add(makeNode(0,0));
		maze[0][0] = 1;
		
		while(!stk.isEmpty())
		{
			Map.Entry<Integer, Integer> next = stk.pop();
			Integer nowX = next.getKey();;
			Integer nowY = next.getValue();
			Integer cValue = maze[nowX][nowY];
			if(move(nowX-1,nowY)){
				if(maze[nowX-1][nowY] > cValue+1)
				{
					maze[nowX-1][nowY] = cValue+1;
					stk.add(makeNode(nowX-1,nowY));
				}
			}
			if(move(nowX+1,nowY)){
				if(maze[nowX+1][nowY] > cValue+1)
				{
					maze[nowX+1][nowY] = cValue+1;
					stk.add(makeNode(nowX+1,nowY));
				}
			}
			if(move(nowX,nowY+1)){
				if(maze[nowX][nowY+1] > cValue+1)
				{
					maze[nowX][nowY+1] = cValue+1;
					stk.add(makeNode(nowX,nowY+1));
				}
			}
			if(move(nowX,nowY-1)){
				if(maze[nowX][nowY-1] > cValue+1)
				{
					maze[nowX][nowY-1] = cValue+1;
					stk.add(makeNode(nowX,nowY-1));
				}
			}
		}
		System.out.println(maze[row-1][column-1]);
	}
	
	public static Map.Entry<Integer, Integer> makeNode(Integer key, Integer value){
		return new AbstractMap.SimpleEntry<Integer,Integer>(key, value);
	}
	public static boolean move(int x, int y) {
		if(x >= row || y >= column || x<0 || y<0){
			return false;
		}else 
			return visited[x][y];
	}
}
