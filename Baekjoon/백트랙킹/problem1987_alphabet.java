import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class problem1987_alphabet {
    public static int[] mx = {-1, 0, 1, 0};
    public static int[] my = {0, 1, 0, -1};
    public static int ans;
    public static int r;
    public static int c;
    // map 보다는 어차피 알파벳이니까 그냥 배열을 사용하는게 편리함
    public static Map<Character, Integer> alphabets;
    public static char[][] maps;
    private static void dfs(int i, int j, int cnt){
        ans = Math.max(ans, cnt);
        for(int k = 0; k < 4; k++){
            int nextX = i + mx[k];
            int nextY = j + my[k];
            if (nextX >= 0 && nextX < r && nextY >= 0 && nextY < c && alphabets.get(maps[nextX][nextY]) == 0){
                alphabets.put(maps[nextX][nextY], alphabets.get(maps[nextX][nextY]) + 1);
                cnt += 1;
                dfs(nextX, nextY, cnt);
                alphabets.put(maps[nextX][nextY], alphabets.get(maps[nextX][nextY]) - 1);
                cnt -= 1;
            }
        }
    }
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        ans = 0;
        maps = new char[r][c];
        alphabets = new HashMap<>();
        for(int i = 0; i < r; i++){
            String t = br.readLine();
            for(int j = 0; j < c; j++){
                maps[i][j] = t.charAt(j);
                if(!alphabets.containsKey(maps[i][j])){
                    alphabets.put(maps[i][j], 0);
                }
            }
        }
        alphabets.put(maps[0][0], alphabets.get(maps[0][0]) + 1);
        dfs(0, 0, 1);
        System.out.println(ans);
    }
}