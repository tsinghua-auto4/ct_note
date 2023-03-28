package _230328;

import java.util.Scanner;

public class Main_1411_IM_두줄로타일깔기_이경훈 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long[] dp = new long[100001];
		dp[1] = 1;
		dp[2] = 3;
		int n = 3;
		while (n < N + 1) {
			dp[n] = ((2 * dp[n - 2]) % 20100529 + dp[n - 1]) % 20100529;
			n++;
		}

		System.out.println(dp[N] % 20100529);
	}
}
