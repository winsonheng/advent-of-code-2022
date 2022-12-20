import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Day20Part1 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        String fileName = "20.in";
        BufferedReader br = new BufferedReader(new FileReader(fileName));
        
        ArrayList<Node> nodes = new ArrayList<>();
        Node ptr = null, head = null, nodeZero = null;
        String line;
        while ((line = br.readLine()) != null) {
            if (ptr == null) {
                ptr = head = new Node(Integer.parseInt(line));
            } else {
                Node newNode = new Node(Integer.parseInt(line));
                newNode.prev = ptr;
                ptr.next = newNode;
                ptr = newNode;
            }

            nodes.add(ptr);

            if (ptr.val == 0) {
                nodeZero = ptr;
            }
        }
        br.close();
        ptr.next = head;
        head.prev = ptr;

        int maxMoves = nodes.size() - 1;
        for (Node node: nodes) {
            int numMoves = node.val >= 0 ? node.val % maxMoves : maxMoves + node.val % maxMoves;
            if (numMoves == 0) {
                continue;
            }
            ptr = node;
            if (numMoves <= maxMoves / 2) { // Move forward
                for (int i = 0; i < numMoves; ++i) {
                    ptr = ptr.next;
                }
                // Deletion of current node
                node.prev.next = node.next;
                node.next.prev = node.prev;
                // Insertion of current node
                ptr.next.prev = node;
                node.next = ptr.next;
                ptr.next = node;
                node.prev = ptr;
            } else { // Move backwards max - n times
                for (int i = 0; i < maxMoves - numMoves; ++i) {
                    ptr = ptr.prev;
                }
                // Deletion of current node
                node.prev.next = node.next;
                node.next.prev = node.prev;
                // Insertion of current node
                ptr.prev.next = node;
                node.prev = ptr.prev;
                ptr.prev = node;
                node.next = ptr;
            }
        }

        ptr = nodeZero;
        int ans = 0;
        for (int count = 0; count < 3; ++count) {
            for (int i = 0; i < 1000; ++i) {
                ptr = ptr.next;
            }
            ans += ptr.val;
        }
        System.out.println(ans);
    }

    public static class Node {
        int val;
        Node prev, next;
        public Node(int v) {
            val = v;
        }
    }
}