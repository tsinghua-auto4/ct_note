package _230328;

import java.util.Scanner;

public class Main_1463_S3_1로만들기_이경훈 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		int[] dp = new int[1000001];
		dp[1] = 0;
		dp[2] = 1;
		dp[3] = 1;
		dp[4] = 2;
		for (int n = 3; n <= N; n++) {
			dp[n] = Math.min(dp[n - 1] + 1, Math.min(dp[n / 3] + 1 + n % 3, dp[n / 2] + 1 + n % 2));
		}
		
		System.out.println(dp[N]);
	}
}
