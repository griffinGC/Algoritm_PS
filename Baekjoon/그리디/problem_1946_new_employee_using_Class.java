package Baekjoon;

import java.util.*;

public class problem1946_new_employee_upgrade {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int caseN = sc.nextInt();
        ArrayList<Grade> gList = new ArrayList<>();
        for(int i = 0; i < caseN; i++){
            int n = sc.nextInt();
            for(int j = 0; j<n; j++){
                int a = sc.nextInt();
                int b = sc.nextInt();
                gList.add(new Grade(a,b));
            }
            Collections.sort(gList, new Comparator<Grade>() {
                @Override
                public int compare(Grade o1, Grade o2) {
                    return o1.first - o2.first;
                }
            });
            int cnt = 0, min = n+1;
            for(int k = 0; k<gList.size(); k++){
                int second = gList.get(k).second;
                if(min > second){
                    cnt++;
                    min = second;
                }
            }
            System.out.println(cnt);
            gList.clear();
        }
    }
}

class Grade{
    int first;
    int second;
    Grade(int first, int second){
        this.first = first;
        this.second = second;
    }
}