import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Day2Part2 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        BufferedReader br = new BufferedReader(new FileReader("2.in"));
        int score = 0;

        String line;
        while ((line = br.readLine()) != null) {
            char[] input = line.toCharArray();
            switch (input[2]) {
                case 'X':
                    score += 1 + (input[0] - 63) % 3;
                    break;
                case 'Y':
                    score += 3 + input[0] - 64;
                    break;
                case 'Z':
                    score += 7 + (input[0] - 64) % 3;
                    
            }
        }

        System.out.println(score);
        br.close();
    }
}
