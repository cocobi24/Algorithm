/* https://www.acmicpc.net/problem/2164 */

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        Deque<Integer> dq = new LinkedList<>();

        for(int i=1; i<=n; i++){
            dq.add(i);
        }

        while(dq.size()>1){
            dq.pollFirst();
            dq.add(dq.pollFirst());
        }

        System.out.print(dq.peek());
    }
}