# https://www.acmicpc.net/problem/2163

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int m = s.nextInt();
        int answer = (n*m) - 1;
        System.out.println(answer);
    }
}