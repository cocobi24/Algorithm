/* https://www.acmicpc.net/problem/5355 */

import java.io.*;

public class Main {
    public static void main(String[] agrs) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++) {
            String[] 수식 = br.readLine().split(" ");
            float num = Float.parseFloat(수식[0]);
            for(int j=1; j<수식.length; j++){
                if(수식[j].equals("@")){
                    num *= 3;
                } else if(수식[j].equals("%")){
                    num += 5;
                } else if(수식[j].equals("#")){
                    num -= 7;
                }
            }
            System.out.println(String.format("%.2f",num));
        }
    }
}
