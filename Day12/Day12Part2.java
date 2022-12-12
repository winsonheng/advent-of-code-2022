import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;

public class Day12Part2 {
    // L,U,R,D followed by row_offset, col_offset
    private static final int[][] ADJACENT_OFFSET = new int[][] {
        {0, -1},
        {-1, 0},
        {0, 1},
        {1, 0}
    };
    public static void main(String[] args) throws FileNotFoundException, IOException {
        BufferedReader br = new BufferedReader(new FileReader("12.in"));
        ArrayList<String> grid = new ArrayList<String>();
        int sRow = 0, sCol = 0, eRow = 0, eCol = 0;
        
        String line;
        while ((line = br.readLine()) != null) {
            int index = line.indexOf('S');
            if (index >= 0) {
                sRow = grid.size();
                sCol = index;
            }
            index = line.indexOf('E');
            if (index >= 0) {
                eRow = grid.size();
                eCol = index;
            }
            grid.add(line);
        }
        br.close();

        int rows = grid.size(), cols = grid.get(0).length();
        // 0: L, 1: U, 2: R, 3: D
        boolean[][][] adjMatrix = new boolean[rows][cols][4];

        // Create adj mat for first row
        String curRow = grid.get(0);
        for (int i = 0; i < cols - 1; ++i) {
            char a = convertChar(curRow.charAt(i)), b = convertChar(curRow.charAt(i + 1));
            if (b - a <= 1) {
                adjMatrix[0][i][2] = true;
            }
            if (a - b <= 1) {
                adjMatrix[0][i + 1][0] = true;
            }
        }

        String prevRow;
        // Create adj mat for row 1 to rows - 1
        for (int i = 1; i < rows; ++i) {
            prevRow = grid.get(i - 1);
            curRow = grid.get(i);
            char up = convertChar(prevRow.charAt(0)), cur = convertChar(curRow.charAt(0)), left;
            if (cur - up <= 1) {
                adjMatrix[i - 1][0][3] = true;
            }
            if (up - cur <= 1) {
                adjMatrix[i][0][1] = true;
            }
            for (int j = 1; j < cols; ++j) {
                up = convertChar(prevRow.charAt(j));
                cur = convertChar(curRow.charAt(j));
                left = convertChar(curRow.charAt(j - 1));
                if (cur - up <= 1) {
                    adjMatrix[i - 1][j][3] = true;
                }
                if (up - cur <= 1) {
                    adjMatrix[i][j][1] = true;
                }
                if (cur - left <= 1) {
                    adjMatrix[i][j - 1][2] = true;
                }
                if (left - cur <= 1) {
                    adjMatrix[i][j][0] = true;
                }
            }
        }

        int shortestPath = rows * cols;

        for (int i = 0; i < rows; ++i) {
            String curString = grid.get(i);
            for (int j = 0; j < cols; ++j) {
                if (curString.charAt(j) != 'a' && curString.charAt(j) != 'S') {
                    continue;
                }

                int[][] distance = new int[rows][cols];
                boolean[][] visited = new boolean[rows][cols];

                // Each element in the queue is a pair containing two connected vertices
                LinkedList<Pair<Integer>> queue = new LinkedList<>();

                // Source vertex distance is 0
                distance[i][j] = 0;
                visited[i][j] = true;
                queue.offer(new Pair<Integer>(i, j));

                // BFS from S
                while (!queue.isEmpty()) {
                    Pair<Integer> edge = queue.poll();
                    int bRow = edge.a, bCol = edge.b;
                    // Found endpoint
                    if (bRow == eRow && bCol == eCol) {
                        shortestPath = Math.min(shortestPath, distance[eRow][eCol]);
                        break;
                    }
                    for (int k = 0; k < 4; ++k) {
                        if (adjMatrix[bRow][bCol][k] && !visited[bRow + ADJACENT_OFFSET[k][0]][bCol + ADJACENT_OFFSET[k][1]]) {
                            distance[bRow + ADJACENT_OFFSET[k][0]][bCol + ADJACENT_OFFSET[k][1]] = distance[bRow][bCol] + 1;
                            visited[bRow + ADJACENT_OFFSET[k][0]][bCol + ADJACENT_OFFSET[k][1]] = true;
                            queue.offer(new Pair<Integer>(bRow + ADJACENT_OFFSET[k][0], bCol + ADJACENT_OFFSET[k][1]));
                        }
                    }
                }
            }
        }
        
        System.out.println(shortestPath);
    }

    static char convertChar(char c) {
        if (c == 'S') {
            return 'a';
        } else if (c == 'E') {
            return 'z';
        }
        return c;
    }

    static class Pair<T> {
        T a, b;
        public Pair(T a, T b) {
            this.a = a;
            this.b = b;
        }

        @Override
        public String toString() {
            return a + ", " + b;
        }
    }
}
