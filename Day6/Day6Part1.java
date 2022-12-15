import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Day6Part1 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        String fileName = "6.in";
        BufferedReader br = new BufferedReader(new FileReader(fileName));
        
        String line = br.readLine();
        br.close();

        for (int i = 3; i < line.length(); ++i) {
            char c0 = line.charAt(i - 3), c1 = line.charAt(i - 2), c2 = line.charAt(i - 1), c3 = line.charAt(i);
            if (c3 == c2) {
                i += 2;
            } else if (c3 == c1 || c2 == c1) {
                i += 1;
            } else if (c3 == c0 || c2 == c0 || c1 == c0) {
                continue;
            } else {
                System.out.println(i + 1);
                return;
            }
                
        }
    }
}
