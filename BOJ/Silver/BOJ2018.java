/* https://www.acmicpc.net/problem/2018 */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int start=1, end=1, sum = 1, count = 1;

        while(end != n){
            if(sum == n) {
                count++;
                end++;
                sum += end;
            } else if(sum > n){
                sum -= start;
                start++;
            } else if(sum < n){
                end++;
                sum += end;
            }
        }

        System.out.print(count);

    }
}