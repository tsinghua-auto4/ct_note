import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(br.readLine());
		ArrayList<Integer> list = new ArrayList<>();
		ArrayDeque<int[]> stk = new ArrayDeque<>();
		StringTokenizer st = new StringTokenizer(br.readLine());
		stk.push(new int[] { 0, 0 });
		// 리스트에 입력값 다 넣어 놓
		for (int i = 0; i < N; i++) {
			list.add(Integer.parseInt(st.nextToken()));
		}
		// 스택을 이용
		for (int i = 0; i < N; i++) {
			// 만약 스택의 top값보다 리스트의 값이 더 크거나 같다
			while (!stk.isEmpty()) {
				if (list.get(i) >= stk.peekLast()[0]) {
					stk.pollLast();
				} else {
					sb.append(stk.peekLast()[1] + 1).append(" ");
					stk.offer(new int[] { list.get(i), i });
					break;
				}
			}
			if (stk.isEmpty()) {
				sb.append(0).append(" ");
				stk.offer(new int[] { list.get(i), i });
			}
		}
		System.out.println(sb.toString());
	}
}