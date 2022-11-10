/* https://www.acmicpc.net/problem/11047 */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int money = Integer.parseInt(st.nextToken());
        List<Integer> coins = new ArrayList<>();
        int answer = 0;

        for(int i=0; i<n; i++){
            coins.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(coins, Collections.reverseOrder());

        for(int coin : coins){
            if(coin > money){
                continue;
            }
            answer += money/coin;
            money = money % coin;
        }
        System.out.print(answer);
    }
}