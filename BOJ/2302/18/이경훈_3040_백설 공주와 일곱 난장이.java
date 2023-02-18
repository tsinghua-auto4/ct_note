import java.util.Scanner;

public class Main {
	static int[] shorts;
	static int[] ans;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		shorts = new int[9];
		ans = new int[7];
		for (int i = 0; i < 9; i++) {
			shorts[i] = sc.nextInt();
		}

		combi(0, 0, 0);
	}

	private static void combi(int cnt, int start, int sum) {
		if (sum > 100) {
			return;
		}
		if (cnt == 7) {
			if (sum == 100) {
				for (int i : ans) {
					System.out.println(i);
				}
			}
			return;
		}

		for (int i = start; i < 9; i++) {
			ans[cnt] = shorts[i];
			combi(cnt + 1, i + 1, sum + shorts[i]);

		}
	}
}