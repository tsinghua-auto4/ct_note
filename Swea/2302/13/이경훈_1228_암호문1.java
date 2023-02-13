import java.util.LinkedList;
import java.util.Scanner;

public class 이경훈_1228_암호문1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		LinkedList<Integer> pwList;
		StringBuilder sb;
		// 테스트케이스 반복
		for (int tc = 1; tc <= 10; tc++) {
			pwList = new LinkedList<>();
			sb = new StringBuilder();
			int N = sc.nextInt();
			// 연결리스트에 입력
			for (int i = 0; i < N; i++) {
				pwList.add(sc.nextInt());
			}

			// idx번째 뒤에 n개의 입력만큼 삽입
			int times = sc.nextInt();
			for (int t = 0; t < times; t++) {
				sc.next();
				int idx = sc.nextInt();
				int n = sc.nextInt();
				for (int i = idx; i < idx + n; i++) {
					pwList.add(i, sc.nextInt());
				}
			}
			// 출력
			sb.append('#').append(tc).append(" ");
			for (int i = 0; i < 10; i++) {
				sb.append(pwList.poll()).append(" ");
			}
			System.out.println(sb.toString());
		}

	}
}
