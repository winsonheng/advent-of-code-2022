import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.PriorityQueue;

public class Day1Part2 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        BufferedReader br = new BufferedReader(new FileReader("1-2.in"));
        PriorityQueue<Integer> pq = new PriorityQueue<>(3);
        
        String inputLine;
        int current = 0;
        while ((inputLine = br.readLine()) != null) {
            if (inputLine.isEmpty()) {
                if (pq.size() < 3) {
                    pq.offer(current);
                } else if (current > pq.peek()) {
                    pq.poll();
                    pq.offer(current);
                }
                current = 0;
            } else {
                current += Integer.parseInt(inputLine);
            }
        }

        int sum = 0;
        while (pq.peek() != null) {
            sum += pq.poll();
        }
        System.out.println(sum);

        br.close();
    }
}
