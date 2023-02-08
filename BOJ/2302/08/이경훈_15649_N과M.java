import java.util.Scanner;

public class 이경훈_15649_N과M {
	static int N;
	static int M;
	static boolean[] selected;
	static int[] numbers;
	static StringBuilder sb;

	static void perm(int cnt) {
		if (cnt == M) {
			for (int i : numbers) {
				sb.append(i).append(" ");
			}
			sb.append("\n");
			return;
		}

		for (int i = 1; i <= N; i++) {
			if (selected[i])
				continue;
			numbers[cnt] = i;
			selected[i] = true;
			perm(cnt + 1);
			selected[i] = false;
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		numbers = new int[M];
		selected = new boolean[N + 1];
		sb = new StringBuilder();

		perm(0);
		System.out.println(sb.toString());
	}
}