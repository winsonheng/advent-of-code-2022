import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashSet;

public class Day3Part1 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        BufferedReader br = new BufferedReader(new FileReader("3.in"));
        int sum = 0;
        
        String line;
        while ((line = br.readLine()) != null) {
            HashSet<Character> set = new HashSet<>();
            int i = 0;
            for (; i < line.length() / 2; ++i) {
                set.add(line.charAt(i));
            }
            for (; i < line.length(); ++i) {
                char c = line.charAt(i);
                if (set.contains(c)) {
                    sum += c >= 'a' ? c - 'a' + 1 : c - 'A' + 27;
                    break;
                }
            }
        }

        System.out.println(sum);
        br.close();
    }
}
