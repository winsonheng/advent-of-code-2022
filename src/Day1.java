import java.net.*;
import java.io.*;

public class Day1 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        BufferedReader in = new BufferedReader(new FileReader(new File("in.txt")));

        int highest = 0, current = 0;
        String inputLine;
        while ((inputLine = in.readLine()) != null) {
            if (inputLine.isEmpty()) {
                highest = Math.max(highest, current);
                current = 0;
            } else {
                current += Integer.parseInt(inputLine);
            }
        }
        in.close();

        System.out.println(highest);
    }
}
