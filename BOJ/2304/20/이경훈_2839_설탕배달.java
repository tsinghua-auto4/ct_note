package _230328;

import java.util.Arrays;
import java.util.Scanner;

public class Main_2839_S4_설탕배달_이경훈 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] dp = new int[5001];
		Arrays.fill(dp, 10000000);
		dp[3] = 1;
		dp[5] = 1;
		for (int n = 6; n <= 5000; n++) {
			dp[n] = Math.min(dp[n - 3] + 1, dp[n - 5] + 1);
		}
		if (dp[N] >= 1000000)
			System.out.println(-1);
		else
			System.out.println(dp[N]);
	}
}
