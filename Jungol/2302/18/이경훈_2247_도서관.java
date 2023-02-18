import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class 이경훈_2247_도서관 {
	static int pre_start;
	static int pre_end;
	static int post_start;
	static int post_end;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		List<int[]> candidate = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			candidate.add(new int[] { sc.nextInt(), sc.nextInt() });
		}
		Collections.sort(candidate, new Comparator<int[]>() {

			@Override
			public int compare(int[] o1, int[] o2) {
				return o1[0] - o2[0];
			}
		});
//		for (int[] is : candidate) {
//			System.out.println(Arrays.toString(is));
//		}
		int occupiedTime = 0;
		int vacantTime = candidate.get(0)[0];

		for (int[] is : candidate) {
			post_start = is[0];
			post_end = is[1];

			if (pre_end >= post_start) { // 만약 전의 end가 현재의 start보다 크거나 같다면
				occupiedTime = Math.max(occupiedTime, Math.max(post_end, pre_end) - pre_start);
				pre_end = Math.max(post_end, pre_end);
			} else if (pre_end < post_start) { // 만약 전의 end가 현재의 start보다 작다면
				vacantTime = Math.max(vacantTime, post_start - pre_end);
				pre_start = post_start;
				pre_end = post_end;
			}
		}
		System.out.printf("%d %d", occupiedTime, vacantTime);
	}
}
