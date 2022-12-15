import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;

public class Day6Part2 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        String fileName = "6.in";
        BufferedReader br = new BufferedReader(new FileReader(fileName));
        
        String line = br.readLine();
        br.close();

        HashMap<Character, Integer> map = new HashMap<>();
        final int PACKET_LENGTH = 14;

        for (int i = 0; i < PACKET_LENGTH; ++i) {
            map.merge(line.charAt(i), 1, (v, x) -> v + 1);
        }

        if (map.size() == PACKET_LENGTH) {
            System.out.println(PACKET_LENGTH);
            return;
        }

        for (int i = PACKET_LENGTH; i < line.length(); ++i) {
            map.merge(line.charAt(i - PACKET_LENGTH), 0, (v, x) -> v == 1 ? null : v - 1);
            map.merge(line.charAt(i), 1, (v, x) -> v + 1);

            if (map.size() == PACKET_LENGTH) {
                System.out.println(i + 1);
                break;
            }
        }
    }
}
