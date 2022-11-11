/* https://www.acmicpc.net/problem/1940 */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        int start = 0, end = n-1, count=0;
        while(start < end){
            if(arr[start] + arr[end] > m) {
                end--;
            } else if(arr[start] + arr[end] < m){
                start++;
            } else if(arr[start] + arr[end] == m){
                count++;
                start++;
                end--;
            }
        }

        System.out.print(count);

    }
}