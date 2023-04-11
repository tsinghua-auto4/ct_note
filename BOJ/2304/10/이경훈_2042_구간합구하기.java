package _230407;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_2042_G1_구간합구하기_이경훈 {
	static int N, M, K;
	static long[] tree;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		long[] nums = new long[N];
		for (int i = 0; i < N; i++) {
			nums[i] = Long.parseLong(br.readLine());
		}
		tree = new long[N + 1];

		for (int i = 1; i <= N; i++) {
			update(i, nums[i - 1]);
		}

		for (int i = 0; i < M + K; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			long c = Long.parseLong(st.nextToken());
			if (a == 1) {
				update(b, c - nums[b - 1]);
				nums[b - 1] = c;
			} else {
				System.out.println(sum(b, (int) c));
			}

		}

	}

	/**
	 * 
	 * 입력값으로 tree를 구성하는 함수
	 */
	public static void update(int i, long num) {
		while (i <= N) {
			tree[i] += num;
			i += (i & -i); // 다음 위치에 데이터를 update 다음 update할 위치 => index+k
		}
	}

	/**
	 * 1~i 까지의 구간 합 구하기
	 */
	public static long sum(int i) {
		long ans = 0;
		while (i > 0) {
			ans += tree[i];
			i -= (i & -i); // 이전 구간의 합이 있는 위치로 이동 이전 구간 합이 있는 위치 => index-k
		}
		return ans;
	}

	/**
	 * start ~ end 까지의 구간 합 구하기
	 */
	public static long sum(int start, int end) {
		return sum(end) - sum(start - 1);
	}

}
