public class Main_15650_S3_N과M2_이경훈 {
	static int[] numbers;
	static int M;
	static int N;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		numbers = new int[M];

		solve(0, 1);
	}

	public static void solve(int idx, int start) {
		if (idx == M) {
			for (int i = 0; i < numbers.length; i++) {
				System.out.print(numbers[i] + " ");
			}
			System.out.println();
			return;
		}
		for (int i = start; i <= N; i++) {
			numbers[idx] = i;
			solve(idx + 1, i + 1);
		}
	}
}
