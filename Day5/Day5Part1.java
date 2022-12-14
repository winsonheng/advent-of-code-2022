import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.stream.Stream;

public class Day5Part1 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        String fileName = "5.in";
        BufferedReader br = new BufferedReader(new FileReader(fileName));
        ArrayList<LinkedList<Character>> arr = new ArrayList<>();
        arr.add(null);
        
        String line;
        while ((line = br.readLine()).startsWith("[") || line.startsWith("   ")) {
            String[] split = line.replaceAll("    ", " []").split(" ");
            for (int i = 0; i < split.length; ++i) {
                if (arr.size() == i + 1) {
                    arr.add(new LinkedList<>());
                }
                if (!split[i].equals("[]")) {
                    arr.get(i + 1).offer(split[i].charAt(1));
                }
            }
        }
        br.readLine();
        while ((line = br.readLine()) != null) {
            // 0: move, 1: from, 2: to indices
            Integer[] indices = Stream.of(line.replaceAll("move |from |to ", "").split(" "))
                                .map(Integer::valueOf).toArray(Integer[]::new);
            for (int i = 0; i < indices[0]; ++i) {
                arr.get(indices[2]).push(arr.get(indices[1]).pop());
            }
            
        }
        br.close();

        for (int i = 1; i < arr.size(); ++i) {
            System.out.print(arr.get(i).pop());
        }
    }
}
