/* https://www.acmicpc.net/problem/1546 */

import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] tempNums = br.readLine().split(" ");
        List<Integer> scores = new ArrayList<>();

        for(String num : tempNums){
            scores.add(Integer.parseInt(num));
        }

        Collections.sort(scores, Collections.reverseOrder());
        float highScore = scores.get(0);
        float sumScore = 0;

        for(int i=0; i<scores.size(); i++){
            sumScore += ((scores.get(i)/highScore)*100);
        }

        System.out.println(sumScore/scores.size());

    }
}