import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashSet;

public class Day3Part2 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        BufferedReader br = new BufferedReader(new FileReader("3.in"));
        int sum = 0;
        
        String line;
        while ((line = br.readLine()) != null) {
            boolean[][] arr = new boolean[2][123];
            for (int i = 0; i < 2; ++i, line = br.readLine()) {
                for (char c: line.toCharArray()) {
                    arr[i][c] = true;
                }
            }
            for (char c: line.toCharArray()) {
                if (arr[0][c] && arr[1][c]) {
                    sum += c > 'a' ? c - 'a' + 1 : c - 'A' + 27;
                    break;
                }
            }
        }

        System.out.println(sum);
        br.close();
    }
}
