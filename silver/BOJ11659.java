/* https://www.acmicpc.net/problem/11659 */

import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] sumArr = new int[n+1];
        int sum = 0;
        int a,b;
        st = new StringTokenizer(br.readLine());
        sumArr[0] = 0;

        for(int i=1; i<n+1; i++){
            sum += Integer.parseInt(st.nextToken());
            sumArr[i] = sum;
        }

        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            System.out.println(sumArr[b]-sumArr[a-1]);
        }

    }
}