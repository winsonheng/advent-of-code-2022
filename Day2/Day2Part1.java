import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Day2Part1 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        BufferedReader br = new BufferedReader(new FileReader("2.in"));
        int[] scoreMap = new int[] {6, 0, 3, 6, 0};
        int score = 0;

        String line;
        while ((line = br.readLine()) != null) {
            char[] input = line.toCharArray();
            score += input[2] - 87 + scoreMap[input[2] - input[0] - 21];
        }

        System.out.println(score);
        br.close();
    }
}
