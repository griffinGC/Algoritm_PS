package Baekjoon;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class problem2667_blockNumber_dfs {
    public static int number = 0;
    public static int[][] map;
    static int[][] visited;
    static int[] x = {-1, 0, 1, 0};
    static int[] y = {0, 1, 0, -1};
    static int n;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        map = new int[n][n];
        visited = new int[n][n];
        for(int i = 0; i<n; i++){
            String line = sc.nextLine();
            for(int j = 0; j<line.length(); j++){
                map[i][j] = line.charAt(j) - '0';
            }
        }
        ArrayList<Integer> numberList = new ArrayList<>();
        for(int i = 0; i<n; i++){
            for(int j = 0; j<n; j++){
                if(map[i][j] == 1 && visited[i][j] == 0){
                    number = 1;
                    dfs(i,j);
                    numberList.add(number);
                }
            }
        }
        Collections.sort(numberList);
        System.out.println(numberList.size());
        for(int number : numberList){
            System.out.println(number);
        }
    }
    //dfs 이용 구현
    public static void dfs(int xNode, int yNode){
        visited[xNode][yNode] = 1;
        for(int i = 0; i<x.length; i++){
            int findX = xNode + x[i];
            int findY = yNode + y[i];
            if(findX>=0 && findY >=0 && findX<n && findY<n && map[findX][findY] == 1 && visited[findX][findY] == 0){
                dfs(findX, findY);
                number++;
            }
        }
    }
}
