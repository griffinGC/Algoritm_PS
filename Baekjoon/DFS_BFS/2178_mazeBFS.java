import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class boj2178_maze {
	static boolean[][] visited;
	static int[][] maze;
	
	//방문하기 위해서 계산함 
	static int dx[] = {-1,0,1,0};
	static int dy[] = {0, -1, 0, 1};
	static int row;
	static int column;

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		row = scan.nextInt();
		column = scan.nextInt();
		maze = new int[row][column];
		String str = "";
		for(int i = 0; i<row; i++) {
			str = scan.next();
//			System.out.println(str);
			for(int j = 0; j<column; j++) 
			{
				//아스키 코드의 '0'을 빼서 일반 숫자로 만들어줌 48대신 '0'을 적어도 됨 
				maze[i][j] = str.charAt(j) - 48;
			}
		}
		visited = new boolean[row][column];
		bfsMaze(0,0);
		System.out.println(maze[row-1][column-1]);		
	}
	
	public static void bfsMaze(int x, int y) {
		visited[x][y] = true;
		Queue<Integer> qx = new LinkedList<Integer>();
		Queue<Integer> qy = new LinkedList<Integer>();
		qx.add(x);
		qy.add(y);
		while(!qx.isEmpty() && !qy.isEmpty()) 
		{
			int nextX = qx.poll();
			int nextY = qy.poll();
			for(int i = 0; i<4; i++) 
			{
				int x1 = nextX+dx[i];
				int y1 = nextY+dy[i];
				//조건 벗어날때는 continue이용해서 이번 반복문 나감 
				if(x1 < 0 || y1 <0 || x1 >= row || y1 >=column)
				{continue;}
				//이미 방문한 노드에 대해서 continue이용해서 건너뜀 
				if(visited[x1][y1] || maze[x1][y1] == 0)
				{continue;}
				qx.add(x1);
				qy.add(y1);
				visited[x1][y1] = true;
				//마지막것에 계속 더해줌 (카운트효과)
				maze[x1][y1] = maze[nextX][nextY] +1;
			}
		}
	}
}
