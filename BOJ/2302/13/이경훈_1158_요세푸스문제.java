import java.util.ArrayDeque;
import java.util.Scanner;

public class 이경훈_1158_요세푸스문제 {
	public static void main(String[] args) {
		ArrayDeque<Integer> ad = new ArrayDeque<>();
		StringBuilder sb = new StringBuilder();
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		// 1부터 N까지의 수 입력
		for (int i = 1; i <= N; i++) {
			ad.add(i);
		}
		sb.append('<');
		// 큐의 사이즈가 0이 되기 직전까지 수행
		while (ad.size() != 0) {
			// 맨 앞에서 빼고 맨 뒤로 붙이는 행위를 K-1 번만큼 수행
			for (int i = 0; i < K - 1; i++) {
				ad.offer(ad.poll());
			}
			// 맨 앞의 요소를 빼서 sb에 입력
			sb.append(ad.poll()).append(", ");
		}
		sb.deleteCharAt(sb.length() - 1);
		sb.deleteCharAt(sb.length() - 1);
		sb.append('>');
		System.out.println(sb.toString());
	}
}
