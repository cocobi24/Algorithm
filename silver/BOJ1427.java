/* https://www.acmicpc.net/problem/1427 */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<String> answer = new ArrayList<>();
        String[] nums = br.readLine().split("");
        Arrays.sort(nums);

        for(String s : nums){
            answer.add(s);
        }

        Collections.reverse(answer);
        System.out.print(String.join("", answer));
    }
}