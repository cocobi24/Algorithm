/* https://www.acmicpc.net/problem/2675 */

import java.io.*;

public class Solution {
    public static void main(String[] agrs) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++){
            String[] temp = br.readLine().split(" ");
            int r = Integer.parseInt(temp[0]);
            String[] s = temp[1].split("");

            for(int j=0; j<s.length; j++){
                System.out.print(s[j].repeat(r));
            }
            System.out.print("\n");
        }
    }
}
