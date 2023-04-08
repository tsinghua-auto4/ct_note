package _230406;

import java.util.Scanner;

public class Solution_5607_D3_조합_이경훈 {
	static final int P = 1234567891;
	static int N, R;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

		// 미리 팩토리얼 배열 만들어놓기
		long fac[] = new long[1000001];
		fac[0] = 1;
		for (int i = 1; i <= 1000000; i++) {
			fac[i] = (fac[i - 1] * i) % P;
		}

		for (int tc = 1; tc <= T; tc++) {
			N = sc.nextInt();
			R = sc.nextInt();

			long base = (fac[R] * fac[N - R]) % P;
			long what = divide(base, P - 2);

			System.out.println("#" + tc + " " + (fac[N] * what) % P);
		}
	}

	private static long divide(long base, int ex) {
		if (ex == 0)
			return 1;
		long tmp = divide(base, ex / 2);

		long ret = (tmp * tmp) % P;
		if (ex % 2 == 0)
			return ret;
		else
			return (ret * base) % P;
	}
}
