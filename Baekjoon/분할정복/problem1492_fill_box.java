package Baekjoon;

import java.io.*;
import java.util.*;

public class problem1492_fill_box {
    public static int cnt = 0;
    public static boolean check = true;
    public static int[] cube = new int[20];
    public static List<Pair> v = new ArrayList<Pair>();

    public static void fill(int l, int w, int h, int idx){
        if(l == 0 || w == 0 || h == 0){
            return;
        }
        for(int i = idx; i < v.size(); i++){
            Pair nowV = v.get(i);
            if(nowV.number != 0 && nowV.side <= l && nowV.side <= w && nowV.side <= h){
                nowV.number--;
                cnt++;
                // 넣을 수 있는지 여부 확인 및 가능하다면 넣는 형태
                fill(l - nowV.side, w, h, i);
                fill(nowV.side, w - nowV.side, h, i);
                fill(nowV.side, nowV.side, h - nowV.side, i);
                return;
            }
        }
        check = false;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int l, w, h, n;
        l = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(br.readLine());
        ;

        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            cube[a] = b;
        }
        for(int i = 19; i >= 0; i --){
            if(cube[i] != 0){
                v.add(new Pair((int) Math.pow(2, i), cube[i]));
            }
        }
        fill(l, w, h, 0);
        if(!check){
            System.out.println(-1);
        }else{
            System.out.println(cnt);
        }
    }
}
class Pair{
    int side, number;
    public Pair(int side, int number){
        this.side = side;
        this.number = number;
    }
}