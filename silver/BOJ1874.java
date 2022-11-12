/* https://www.acmicpc.net/problem/1874 */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        int n = Integer.parseInt(br.readLine());
        Stack<Integer> st = new Stack<>();
        int target;
        int num = 1;
        int top = 0;
        int flag = 0;

        for(int i=0; i<n; i++){
            target = Integer.parseInt(br.readLine());

            if(target >= num) {
                while (target >= num) {
                    st.add(num++);
                    sb.append("+\n");
                }
                st.pop();
                sb.append("-\n");
            } else {
                top = st.pop();
                if(top > target){
                    System.out.println("NO");
                    flag++;
                    break;
                } else {
                    sb.append("-\n");
                }
            }
        }

        if(flag == 0) {
            System.out.println(sb.toString());
        }
    }
}