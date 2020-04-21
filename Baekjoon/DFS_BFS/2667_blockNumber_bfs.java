package Baekjoon;

import java.lang.reflect.Array;
import java.util.*;

public class problem2667_blockNumber_bfs {
    static int n = 0;
    static int[][] map;
    static int[][] visited;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int count = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        map = new int[n][n];
        visited = new int[n][n];
        sc.nextLine();

        for(int i = 0; i < n; i++) {
            String line = sc.nextLine();
            for (int j = 0; j < line.length(); j++) {
                map[i][j] = line.charAt(j) - '0';
            }
        }
        ArrayList<Integer> numberList = new ArrayList<>();
        for(int i = 0; i<n; i++){
            for(int j = 0; j<n; j++){
                if(map[i][j] == 1 && visited[i][j] == 0){
                    count = 0;
                    bfs(i,j);
                    numberList.add(count);
                }
            }
        }

        Collections.sort(numberList);
        System.out.println(numberList.size());
        for(int ele : numberList){
            System.out.println(ele);
        }

    }
    public static int bfs(int x, int y){
        ArrayList<Integer> numberList = new ArrayList<Integer>();
        Queue<Position> qList = new LinkedList<>();
        qList.add(new Position(x,y));
        while(!qList.isEmpty()){
            Position cur = qList.poll();
            if(visited[cur.x][cur.y] == 1){
                continue;
            }
            visited[cur.x][cur.y] = 1;
            count++;
            for(int i = 0; i<dx.length; i++){
                int mX = cur.x + dx[i];
                int mY = cur.y + dy[i];
                if(mX >= 0 && mY >=0 && mX <n && mY<n && map[mX][mY] == 1 && visited[mX][mY] == 0){
                    qList.add(new Position(mX, mY));
                }
            }
        }
        return count;
    }
}

class Position{
    int x, y;
    Position(int x, int y){
        this.x = x;
        this.y = y;
    }
}