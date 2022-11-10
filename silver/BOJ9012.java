/* https://www.acmicpc.net/problem/9012 */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Stack<String> stack = null;
        String prev = null;
        String answer = null;

        for(int i=0; i<n; i++){
            String[] target = br.readLine().split("");
            stack = new Stack<>();

            for(int j=0; j<target.length; j++){
                if(target[j].equals("(")){
                    stack.push(target[j]);
                } else {
                    if(stack.size() >= 1){
                        prev = stack.peek();
                        if(prev.equals("(")){
                            stack.pop();
                        }
                    } else {
                        stack.push(target[j]);
                    }
                }
            }
            answer = stack.size() == 0 ? "YES" : "NO";
            System.out.println(answer);
        }
    }
}