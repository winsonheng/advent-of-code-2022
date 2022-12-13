import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.stream.Stream;

public class Day4Part1 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        String fileName = "4.in";
        BufferedReader br = new BufferedReader(new FileReader(fileName));
        int count = 0;
        
        String line;
        while ((line = br.readLine()) != null) {
            String[] split = line.split(",");
            Integer[] first = Stream.of(split[0].split("-")).map(Integer::valueOf).toArray(Integer[]::new);
            Integer[] second = Stream.of(split[1].split("-")).map(Integer::valueOf).toArray(Integer[]::new);
            if (first[0] >= second[0] && first[1] <= second[1] || second[0] >= first[0] && second[1] <= first[1]) {
                ++count;
            }
        }
        br.close();

        System.out.println(count);
    }
}
