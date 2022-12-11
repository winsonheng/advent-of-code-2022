import java.net.*;
import java.io.*;

public class Day1Part1 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        BufferedReader br = new BufferedReader(new FileReader("1-1.in"));

        int highest = 0, current = 0;
        String inputLine;
        while ((inputLine = br.readLine()) != null) {
            if (inputLine.isEmpty()) {
                highest = Math.max(highest, current);
                current = 0;
            } else {
                current += Integer.parseInt(inputLine);
            }
        }
        br.close();

        System.out.println(highest);
    }
}
