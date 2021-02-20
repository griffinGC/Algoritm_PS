import java.util.Scanner;

public class problem15649_NandM {
    static void permutation(int[] arr, boolean[] isUsed, int n, int k, int count){
        if(count == k){
            printArray(arr);
            System.out.println();
            return;
        }
        for(int i = 0; i<n; i++){
            if(!isUsed[i]){
                arr[count] = i+1;
                isUsed[i] = true;
                permutation(arr, isUsed, n, k, count+1);
                isUsed[i] = false;
            }
        }
    }
    static void printArray(int[] arr){
        for(int ele : arr){
            System.out.print(ele + " ");
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        boolean[] isUser = new boolean[n];
        int[] arr = new int[k];
        // 넣을 index, depth, 현재 들어간 갯수

        permutation(arr, isUser, n, k, 0);
    }
}