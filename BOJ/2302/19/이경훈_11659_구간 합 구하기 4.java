import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class test1 {
	static int N;
	static int M;
	static int[] prefix_sum;
	static int[] N_data;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		N_data = new int[N];
		prefix_sum = new int[N + 1];
		st = new StringTokenizer(br.readLine());
		int start = 0, end = 0;
		StringBuilder sb = new StringBuilder();

		// 입력
		for (int i = 0; i < N; i++) {
			N_data[i] = Integer.parseInt(st.nextToken());
		}

		// 구간합 구하기
		for (int i = 1; i <= N; i++) {
			prefix_sum[i] = prefix_sum[i - 1] + N_data[i - 1];
		}
		// 구간 입력받기
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			start = Integer.parseInt(st.nextToken()) - 1;
			end = Integer.parseInt(st.nextToken());

			int left = prefix_sum[start];
			int right = prefix_sum[end];
			sb.append(right - left).append("\n");
		}
		System.out.println(sb.toString());
	}
}
