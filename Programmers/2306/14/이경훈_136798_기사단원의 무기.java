import java.lang.*;

class Solution {
    public int solution(int number, int limit, int power) {        
        int answer = 0;
        int sum = 0;
        for(int i = 1; i <= number; i++){
            System.out.println(getNum(i));
            if(getNum(i)>limit){
                sum = sum + power;
            }else{
                sum = sum + getNum(i);
            }
        }
        answer = sum;
        return answer;
    }
    
    static int getNum(int n){
        int cnt = 0;
        for(int i = 1; i <= Math.sqrt(n); i++){
            if(n%i==0){
                cnt++;
                if(Math.pow(i,2) < n){
                    cnt++;                        
                }
            }
        }
        return cnt;
    }
}