/* https://www.acmicpc.net/problem/1253 */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        int n = Integer.parseInt(br.readLine());
        long[] nums = new long[n];
        int answer = 0;

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            nums[i] = Long.parseLong(st.nextToken());
        }
        Arrays.sort(nums);

        for(int k=0; k<n; k++){
            long target = nums[k];
            int i=0, j=n-1 ;

            while(i<j){
                if(nums[i] + nums[j] == target){
                    if( i != k && j != k){
                        answer++;
                        break;
                    } else if(i == k){
                        i++;
                    } else if(j == k){
                        j--;
                    }
                } else if(nums[i] + nums[j] < target){
                    i++;
                } else {
                    j--;
                }
            }
        }

        System.out.print(answer);
    }
}